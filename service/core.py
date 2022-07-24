import logging
from http.client import responses
import requests

from service.models import MakeRequestResponse

logger = logging.getLogger(__name__)


def make_request(url: str) -> MakeRequestResponse:
    error_message = ""
    try:
        resp = requests.get(url, timeout=5)
        status_code = resp.status_code
        result_as_text = f"{status_code} / {responses[status_code]}"
        logger.info("Successful rexquest to %s: %s", url, result_as_text)
    except requests.exceptions.ConnectTimeout as tex:
        logger.error("ConnectTimeout for %s - Reason: %s", url, str(tex))
        status_code = -1
        result_as_text = "Timeout"
        error_message = str(tex)
    except requests.exceptions.ConnectionError as cex:
        logger.error("ConnectionError for %s - Reason: %s", url, str(cex))
        status_code = -1
        result_as_text = "Connection Error"
        error_message = str(cex)
    except IOError as ioex:
        logger.error("Ambigous error occurred for %s - Reason: %s", url, str(ioex))
        status_code = -1
        result_as_text = "Request Error"
        error_message = str(ioex)
    response = MakeRequestResponse(url=url, status_code=status_code, message=result_as_text)
    if error_message:
        response.error = error_message
    return response


def slugify_url(url: str) -> str:
    non_url_safe = ['"', '#', '$', '%', '&', '+',
                    ',', '/', ':', ';', '=', '?',
                    '@', '[', '\\', ']', '^', '`',
                    '{', '|', '}', '~', "'"]
    non_safe = [character for character in url if character in non_url_safe]
    if non_safe:
        for i in non_safe:
            text = url.replace(i, '')
    url = u'-'.join(url.split())
    return url
