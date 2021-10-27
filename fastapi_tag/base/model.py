from typing import Optional, Any
from pydantic import BaseModel


class Problem(BaseModel):
    """
    Problem model
    
    Args:
        BaseModel: BaseModel

    Returns:
        Problem: Problem model
    """
    title: str
    status: int
    detail: Any
    type: Optional[str] = None
    instance: Optional[str] = None

    def dict(self, *args, **kwargs):
        """
        dict method
        
        Returns:
            dict: dict
        """
        kwargs.pop("exclude_unset")
        return super().dict(*args, exclude_unset=True, **kwargs)


class Version(BaseModel):
    """
    Version model
    
    Args:
        BaseModel (): BaseModel
    """
    app: str
    api: str


class Contact(BaseModel):
    """
    Contact model
    
    Args:
        BaseModel (): BaseModel

    Returns:
        Contact: Contact model
    """
    name: Optional[str]
    url: Optional[str]
    email: Optional[str]

    def dict(self, *args, **kwargs):
        """
        dict method
        Returns:
            dict: dict
        """
        kwargs.pop("exclude_unset")
        return super().dict(*args, exclude_unset=True, **kwargs)

class Metadata(BaseModel):
    """
    Metadata model
    
    Args:
        BaseModel (): BaseModel
    """
    title: str
    version: Version
    description: Optional[str]
    contact: Contact
    api_id: str
    audience: str