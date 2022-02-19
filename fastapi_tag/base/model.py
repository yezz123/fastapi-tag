from typing import Any, Optional

from pydantic import BaseModel


class Problem(BaseModel):

    title: str
    status: int
    detail: Any
    type: Optional[str] = None
    instance: Optional[str] = None

    def dict(self, *args, **kwargs):
        kwargs.pop("exclude_unset")
        return super().dict(*args, exclude_unset=True, **kwargs)


class Version(BaseModel):

    app: str
    api: str


class Contact(BaseModel):

    name: Optional[str]
    url: Optional[str]
    email: Optional[str]

    def dict(self, *args, **kwargs):
        kwargs.pop("exclude_unset")
        return super().dict(*args, exclude_unset=True, **kwargs)


class Metadata(BaseModel):
    title: str
    version: Version
    description: Optional[str]
    contact: Contact
    api_id: str
    audience: str
