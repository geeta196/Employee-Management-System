# errors.py

from flask import jsonify
import logging

def register_error_handlers(app):

    @app.errorhandler(404)
    def not_found(e):
        logging.error("404 Error")
        return jsonify({"error": "Page Not Found"}), 404

    @app.errorhandler(500)
    def internal_error(e):
        logging.error(f"500 Error: {str(e)}")
        return jsonify({"error": "Internal Server Error"}), 500

    @app.errorhandler(Exception)
    def handle_exception(e):
        logging.error(f"Unhandled Exception: {str(e)}")
        return jsonify({"error": "Something went wrong"}), 500