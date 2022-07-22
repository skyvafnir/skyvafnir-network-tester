from pydantic import BaseModel
from pydantic.fields import Optional


class MakeRequestResponse(BaseModel):
    url: str
    status_code: int
    message: str
    error: Optional[str]


class CheckUrlResponse(MakeRequestResponse):
    status_message: str


class UrlCheckRequest(BaseModel):
    url: str
