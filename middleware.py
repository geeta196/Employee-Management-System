# middleware.py

from flask import request
import logging
import time

def register_middleware(app):

    @app.before_request
    def before_request():
        request.start_time = time.time()
        logging.info(f"Incoming: {request.method} {request.path}")

    @app.after_request
    def after_request(response):
        duration = time.time() - request.start_time
        logging.info(
            f"Completed: {request.method} {request.path} "
            f"Status: {response.status_code} "
            f"Time: {round(duration, 3)} sec"
        )
        return response