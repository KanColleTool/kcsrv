#!/usr/bin/env python3
from app import app

if __name__ == '__main__':
    print("Warning: This is a debugging configuration. Run with the gunicorn script to run in production.")

    app.run(host='0.0.0.0')
