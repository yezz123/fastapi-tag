import pytest
from fastapi.testclient import TestClient

from fastapi_tag.base.model import Contact, Metadata, Version
from fastapi_tag.core.application import Application


@pytest.fixture
def metadata():
    return Metadata(
        title="<title>",
        version=Version(app="v0.1.1", api="v0.1.0"),
        description=None,
        contact=Contact(name="name", url="http://test.com", email=None),
        api_id="49786b4b-1889-46ec-bd72-27f332436e6f",
        audience="company-internal",
    )


@pytest.fixture
def app(metadata):
    return Application("", metadata)


def client(app):
    return TestClient(app)
