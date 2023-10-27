#! /usr/bin/env bash
python -m pip install poetry
python -m pip install poetry-dynamic-versioning
poetry config virtualenvs.in-project true --local
poetry install --with cell_locations,collate,dev
poetry run pre-commit install --install-hooks
