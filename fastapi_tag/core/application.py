from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.exception_handlers import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException

from fastapi_tag.base.model import Metadata, Problem
from fastapi_tag.core._base import app
from fastapi_tag.router.routers import RouteGenerator


async def from_validation_error(_request: Request, exc: RequestValidationError):
    """
    from_validation_error function is used to handle validation error.
    """
    body = jsonable_encoder(
        Problem(title="Validation error", status=400, detail=exc.errors())
    )
    return JSONResponse(status_code=400, content=body)


async def from_http_exception(_request: Request, exc: HTTPException):
    """
    from_http_exception function is used to handle HTTPException error.
    """
    problem = Problem(title=exc.detail, status=exc.status_code, detail={})
    body = jsonable_encoder(problem)
    return JSONResponse(status_code=problem.status, content=body)


class Application(FastAPI):
    """
    Class Application is a FastAPI class that is used to create API application.
    """

    def __init__(self, root: str, metadata: Metadata, **kwargs):
        """
        __init__ function is used to initialize Application class.
        """
        self.root = root
        self.metadata = metadata
        super().__init__(
            root_path="",
            title=metadata.title,
            version=metadata.version.api,
            openapi_url=f"{root}/openapi.json",
            docs_url=f"{root}/docs",
            redoc_url=None,
            **kwargs,
        )
        self.add_exception_handler(RequestValidationError, from_validation_error)
        self.add_exception_handler(HTTPException, from_http_exception)
        self.add(app)

    def add(self, route_generator: RouteGenerator) -> None:
        for route in route_generator.routes(prefix=self.root):
            self.routes.append(route)

    def openapi(self):
        """
        openapi function is used to show OpenAPI specification.
        """
        openapi = super().openapi()
        if self.metadata.contact:
            openapi["info"]["contact"] = self.metadata.contact.dict(exclude_unset=True)
        if self.metadata.api_id:
            openapi["info"]["x-api-id"] = self.metadata.api_id
        if self.metadata.audience:
            openapi["info"]["x-audience"] = self.metadata.audience
        return openapi
