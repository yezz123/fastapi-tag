# FastAPI Tag

[![Tests](https://github.com/yezz123/fastapi-tag/actions/workflows/tests.yml/badge.svg)](https://github.com/yezz123/fastapi-tag/actions/workflows/tests.yml)
[![Publish PyPI 🐍](https://github.com/yezz123/fastapi-tag/actions/workflows/release.yml/badge.svg)](https://github.com/yezz123/fastapi-tag/actions/workflows/release.yml)
[![codecov](https://codecov.io/gh/yezz123/fastapi-tag/branch/main/graph/badge.svg?token=y43lS0Ed2N)](https://codecov.io/gh/yezz123/fastapi-tag)
[![PyPI](https://badge.fury.io/py/fastapi-tag.svg)](https://badge.fury.io/py/fastapi-tag)
[![framework](https://img.shields.io/badge/Framework-FastAPI-blue?style)](https://fastapi.tiangolo.com/)
[![Pypi](https://img.shields.io/pypi/pyversions/fastapi-tag.svg?color=%2334D058)](https://pypi.org/project/fastapi-tag)

<p align="center">
    <em>Documented & Enhance the Metadata of your API ✨</em>
</p>

A simple Package could be added to your FastAPI Project to enhance the metadata of your Project and documenting your API with more information.

---

**Source Code**: <https://github.com/yezz123/fastapi-tag>

**Install the project**: `pip install fastapi-tag`

---

## Features 🎉

- Add a tag to your API, which can be used to filter the API documentation.
- Add a description to your API, which can be used to describe the API.
- Add a version to your API, which can be used to describe the version of the API and app.
- Provide some others features like:
  - `API_id`: A unique identifier for the API.
  - `Audience`: The audience of the API (e.g. `public`, `internal`, `external`).
- Tested in python 3.6 and up.
- Last Version of FastAPI :rocket:

## Usage 📚

- To Identify the Metadata of your API:

```py
from fastapi import FastAPI
from fastapi_tag.base.model import Contact, Metadata, Version
from fastapi_tag.core.application import Application

app = FastAPI()

def metadata(app):
    return Metadata(
        title="Hello World",
        version=Version(app="v0.1.1", api="v0.1.0"),
        description="A simple example of a FastAPI application.",
        contact=Contact(
            name="name",
            url="http://test.com",
            email=None
        ),
        api_id="49786b4b-1889-46ec-bd72-27f332436e6f",
        audience="company-internal",
    )

def app(metadata):
    return Application("", metadata)
```

- We have also `Problem` class thats depends on:
    - `title`: The title of the problem.
    - `status`: The status code of the problem.
    - `detail`: A human-readable explanation specific to this occurrence of the problem.
    - `instance`: A URI reference that identifies the specific occurrence of the problem.
    - `type`: A URI reference that identifies the problem type.

- `NameSpace` is a is a decorator that adds a route generator to the namespace object.

for example:

```py
from fastapi_tag.router.routers import Namespace

route = Namespace([])
```

### Format the code 💅

Execute the following command to apply `pre-commit` formatting:

```bash
make lint
```

## TODO 🚧

- Extend the `Problem` class to add more information.
- Add more features to the `Metadata` class.
- Add more features to the `Version` class.
- Provide a detailed documentation for `fastapi_tag` package.

## License 🍻

This project is licensed under the terms of the MIT license.