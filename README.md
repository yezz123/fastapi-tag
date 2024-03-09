# FastAPI Tag

<p align="center">
<a href="https://github.com/yezz123/fastapi-tag" target="_blank">
    <img src="https://raw.githubusercontent.com/yezz123/fastapi-tag/main/.github/logo.png" alt="FastAPI Tag">
</a>
<p align="center">
    <em>Documented & Enhance the Metadata of your API ✨</em>
</p>
<p align="center">
<a href="https://github.com/yezz123/fastapi-tag/actions/workflows/ci.yml" target="_blank">
    <img src="https://github.com/yezz123/fastapi-tag/actions/workflows/ci.yml/badge.svg" alt="Continuous Integration">
</a>
<a href="https://pypi.org/project/fastapi-tag" target="_blank">
    <img src="https://img.shields.io/pypi/v/pgqb?color=%2334D058&label=pypi%20package" alt="Package version">
</a>
<a href="https://codecov.io/gh/yezz123/fastapi-tag">
    <img src="https://codecov.io/gh/yezz123/fastapi-tag/branch/main/graph/badge.svg"/>
</a>
</p>
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
- Tested in python 3.8 and up.
- Last Version of FastAPI :rocket:

## Usage 📚

- To Identify the Metadata of your API:

```py
from fastapi import FastAPI
from fastapi_tag.model import Contact, Metadata, Version
from fastapi_tag.application import Application

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
from fastapi_tag.routers import Namespace

route = Namespace([])
```

## Development

### Setup environment

You should create a virtual environment and activate it:

> **Notes:** You need to have `python3.9` or higher installed.

I Use `uv` to manage virtual environments, you can install it with:

```bash
# Install uv
pip install uv

# Create a virtual environment
uv venv

# Activate the virtual environment
source .venv/bin/activate
```

And then install the development dependencies:

```bash
# Install dependencies
uv pip install -e .[test,lint]
```

### Run tests 🌝

You can run all the tests with:

```bash
bash scripts/tests.sh
```

### Format the code 🍂

Execute the following command to apply `pre-commit` formatting:

```bash
bash scripts/format.sh
```

## License 🍻

This project is licensed under the terms of the MIT license.
