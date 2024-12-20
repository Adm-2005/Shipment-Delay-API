from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES
from werkzeug.exceptions import HTTPException
from typing import Tuple

def error_response(status_code: int, message: str = None) -> Tuple[dict, int]:
    """
    Creates error response payload with given status code.

    Args
        status_code: HTTP status code
        message: Error message

    Returns
        Tuple[dict, int]: JSON payload and HTTP status code
    """
    payload = {'error': HTTP_STATUS_CODES.get(status_code, 'Unknown Error')}
    
    if message:
        payload['message'] = message

    return jsonify(payload), status_code

def not_found(message: str) -> Tuple[dict, int]:
    """
    Creates a 404 - Not found error response with given message.

    Args
        message: Error message

    Returns
        Tuple[dict, int]: JSON payload and HTTP status code generated from function call
    """
    return error_response(404, message)

def bad_request(message: str) -> Tuple[dict, int]:
    """
    Creates a 400 - Bad Request error response with given message.

    Args
        message: Error message

    Returns 
        Tuple[dict, int]: JSON payload and HTTP status code generated from function call
    """
    return error_response(400, message)

def handle_exception(e: Exception) -> Tuple[dict, int]:
    """
    Creates an error response for the given exception

    Args
        e: Raised exception

    Returns
        Tuple[dict, int]: JSON payload and HTTP status code generated from function call
    """
    if isinstance(e, HTTPException):
        return error_response(e.code, e.description)
    else:
        return error_response(500, str(e))