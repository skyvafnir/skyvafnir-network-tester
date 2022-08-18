import os

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from logging.config import dictConfig
import logging

from skyvafnir_network_test.core import make_request, slugify_url
from skyvafnir_network_test.log_config import configure_logging
from skyvafnir_network_test.models import UrlCheckRequest, CheckUrlResponse

PROJECT_NAME = "skyvafnir-network-test"

# Logging shenanigans
LOG_FORMAT = os.environ.get("LOG_FORMAT", "JSON")
LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")
URL_PATH_PREFIX = os.environ.get("URL_PATH_PREFIX", "")

configure_logging(LOG_FORMAT, LOG_LEVEL)

log = logging.getLogger(PROJECT_NAME)
log.info("Starting up!")
dir_path = os.path.dirname(os.path.realpath(__file__))
templates = Jinja2Templates(directory=f"{dir_path}/templates")

app = FastAPI(
    title=PROJECT_NAME,
    # if not custom domain
    # openapi_prefix="/prod"
)


TEST_URLS = [
    "https://www.google.com",
    "http://localhost:8000/ping",
    "http://bad-url-should-fail.com",
    "http://localhost:8000/check-url",
    "https://www.gzur.org",
]
URLS = os.environ.get("URLS", ",".join(TEST_URLS)).split(",")


@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    checked = []
    version = os.environ.get("VERSION", "no version")
    for url in URLS:
        result = {"name": slugify_url(url), "url": url, "message": "waiting", "result_type": "..."}
        checked.append(result)
    ctx = {"request": request, "results": checked, "urls": URLS, "prefix": URL_PATH_PREFIX, "version": version}
    return templates.TemplateResponse("index.html", ctx)


@app.post("/check-url/", response_model=CheckUrlResponse)
def check_url(url: UrlCheckRequest):
    response = make_request(url.url)
    log.info("Checking URL: %s", url.url)
    if response.status_code == 200:
        status_message = "success"
    elif response.status_code > 0:
        status_message = "warning"
    else:
        status_message = "error"
    return CheckUrlResponse(**response.dict(), status_message=status_message)


@app.get("/ping", summary="Check that the skyvafnir-network-test is operational")
def pong():
    """
    Sanity check - this will let the user know that the skyvafnir-network-test is operational.

    It is also used as part of the HEALTHCHECK. Docker uses curl to check that the API skyvafnir-network-test is still running,
    by exercising this endpoint.

    """
    return {"ping": "pong!"}
