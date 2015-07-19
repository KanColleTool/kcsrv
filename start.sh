#!/usr/bin/env bash

gunicorn -c config_gunicorn.py app:app