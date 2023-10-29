#! /usr/bin/env bash
poetry config virtualenvs.in-project true --local
poetry install --with dev --all-extras
poetry run pre-commit install --install-hooks
