#!/usr/bin/env bash

set -e
set -x

export PYTHONPATH=.
pytest --cov=fastapi_tag --cov=tests