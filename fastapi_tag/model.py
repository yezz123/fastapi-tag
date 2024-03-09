from typing import Any, Optional

from pydantic import BaseModel


class Problem(BaseModel):
    """
    Problem class is a class that is used to describe a problem.
    """

    title: str
    status: int
    detail: Any = None
    type: Optional[str] = None
    instance: Optional[str] = None

    def dict(self, *args, **kwargs):
        """
        dict function is used to return a dictionary.
        """
        kwargs.pop("exclude_unset")
        return super().model_dump(*args, exclude_unset=True, **kwargs)


class Version(BaseModel):
    """
    Version class is a class that is used to describe a version.
    """

    app: str
    api: str


class Contact(BaseModel):
    """
    Contact class is a class that is used to describe a contact.
    """

    name: Optional[str] = None
    url: Optional[str] = None
    email: Optional[str] = None

    def dict(self, *args, **kwargs):
        kwargs.pop("exclude_unset")
        return super().model_dump(*args, exclude_unset=True, **kwargs)


class Metadata(BaseModel):
    """
    Metadata class is a class that is used to describe a metadata.
    """

    title: str
    version: Version
    description: Optional[str] = None
    contact: Contact
    api_id: str
    audience: str
