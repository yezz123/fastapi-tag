from fastapi.testclient import TestClient
from pydantic import BaseModel
from starlette.exceptions import HTTPException

from fastapi_tag.base.model import Problem
from fastapi_tag.router.routers import Namespace, Resource

route = Namespace([])


class Foo(BaseModel):
    bar: int


class Bar(BaseModel):
    foo: str


@route.route("/foo")
class FooResource(Resource):
    async def post(self, _body: Foo) -> Bar:
        return Bar(foo="foo")

    async def get(self):
        raise HTTPException(400, "boom!")


class TestExceptionHandlers:
    def test_validation_error_returns_problem(self, app):
        app.add(route)
        client = TestClient(app)
        resp = client.post("/foo", json={"bar": "bla"})
        obj = resp.json()

        try:
            Problem(**obj)
        except:
            assert False, obj

    def test_http_exception_returns_problem(self, app):
        app.add(route)
        client = TestClient(app)
        resp = client.get("/foo")
        obj = resp.json()

        try:
            Problem(**obj)
        except:
            assert False, obj
