from abc import ABC, abstractmethod
from enum import Enum, auto
from itertools import chain
from typing import Callable, Iterator, List, Optional, Tuple

from fastapi.params import Depends
from fastapi.routing import APIRoute
from starlette.responses import JSONResponse

from fastapi_tag.model import Problem
from fastapi_tag.type import get_return_type as type


class Verb(Enum):
    """
    Verb is an Enum class that is used to describe HTTP verbs.

    Verb is used to describe HTTP verbs.
    """

    GET = auto()
    PUT = auto()
    POST = auto()
    PATCH = auto()
    DELETE = auto()

    @classmethod
    def handler_names(cls) -> Iterator[str]:
        """
        handler_names is a class method that returns the handler names.
        """
        for verb in cls:
            yield verb.handler_name

    @property
    def handler_name(self):
        """
        handler_name is the name of the handler function.
        """
        return self.name.lower()


class RouteGenerator(ABC):
    """
    Abstract class for generating routes.
    """

    @abstractmethod
    def routes(self, tags=None, prefix=None, dependencies=None) -> Iterator[APIRoute]:
        pass


class Namespace(RouteGenerator):
    """
    Namespace.route is a decorator that adds a route generator to the namespace.
    """

    _children: List[RouteGenerator]

    def __init__(
        self,
        tags=None,
        prefix: Optional[str] = None,
        dependencies: Optional[List[Depends]] = None,
    ):
        """
        __init__ is the constructor for Namespace.

        Args:
            tags: A list of tags.
            prefix: A prefix for the namespace.
            dependencies: A list of dependencies.
        """
        self._tags = tags
        self._prefix = prefix
        self._dependencies = dependencies
        self._children = []

    def add(self, route_generator: RouteGenerator) -> None:
        """
        add is a method that adds a route generator to the namespace.
        """
        self._children.append(route_generator)

    def route(self, *args, **kwargs):
        """
        route is a decorator that adds a route generator to the namespace.
        """

        def decorator(cls):
            """
            decorator is a decorator that adds a route generator to the namespace.
            """
            self.add(cls(*args, **kwargs))
            return cls

        return decorator

    def routes(self, tags=None, prefix=None, dependencies=None) -> Iterator[APIRoute]:
        """
        routes is a method that returns the routes.
        """
        tags = (self._tags or []) + (tags or [])
        prefix = "".join(s for s in [prefix, self._prefix] if s is not None)
        dependencies = (self._dependencies or []) + (dependencies or [])
        return chain(
            *[child.routes(tags, prefix, dependencies) for child in self._children]
        )


class Resource(RouteGenerator):
    """
    _RESPONSES is a dictionary of HTTP status codes.
    """

    _RESPONSES = {"4XX": {"model": Problem}}

    def __init__(
        self,
        prefix: Optional[str] = None,
        tags: Optional[List[str]] = None,
        dependencies: Optional[List[Depends]] = None,
    ):
        """
        __init__ is the constructor for Resource.
        """
        self._prefix = prefix
        self._tags = tags
        self._dependencies = dependencies

    def handlers(self) -> Iterator[Tuple[Verb, Callable]]:
        """
        handlers is a method that returns the handlers.
        """
        for verb in Verb:
            if hasattr(self, verb.handler_name):
                yield (verb, getattr(self, verb.handler_name))

    def routes(self, tags=None, prefix=None, dependencies=None) -> Iterator[APIRoute]:
        """
        routes is a method that returns the routes.
        """
        tags = (self._tags or []) + (tags or [])
        prefix = "".join(s for s in [prefix, self._prefix] if s is not None)
        dependencies = (self._dependencies or []) + (dependencies or [])
        for verb, handler in self.handlers():
            yield self._route_from_handler(tags, prefix, verb, handler, dependencies)

    def _route_from_handler(
        self, tags, prefix, verb: Verb, handler, dependencies
    ) -> APIRoute:
        """
        _route_from_handler is a method that returns the route from handler.
        """
        kwargs = {
            "path": prefix,
            "methods": [verb.name],
            "endpoint": handler,
            "summary": handler.__doc__,
            "status_code": 200,
            "tags": tags,
            "response_class": JSONResponse,
            "responses": self._RESPONSES,
            "dependencies": dependencies,
        }

        response_model = type(handler)
        if response_model is not None:
            kwargs["response_model"] = response_model

        return APIRoute(**kwargs)
