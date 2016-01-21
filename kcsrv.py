#!/usr/bin/env python3
import logging

from app import app, logger

root = logging.getLogger()
root.setLevel(logging.DEBUG)

logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)


if __name__ == '__main__':
    logger.warn("This is a debugging configuration. Run with the gunicorn script to run in production.")
    app.run(host='0.0.0.0', debug=True)
