"""Module contains error handlers that works on API level. They catch api, validation and application errors."""
from typing import Tuple, Dict, Any
from marshmallow import ValidationError
from werkzeug.exceptions import HTTPException
from seabattle.helpers.constants import StatusCode


def handle_validation_error(error: ValidationError) -> Tuple[Dict[str, Any], int]:
    """
    Method handles all validation errors.
    Args:
        error: Validation error from marshmallow.

    Returns:
        tuple: Dictionary whit validation error information and status code.
    """
    return {"errors": error.messages,
            "statusCode": StatusCode.VALIDATION_FAILED.value,
            "message": "Validation failed."}, StatusCode.VALIDATION_FAILED.value


def handle_api_error(error: HTTPException) -> Tuple[Dict[str, Any], int]:
    """
    Method handles all API errors.
    Args:
        error: API error.

    Returns:
        tuple: Dictionary whit API error information and status code.
    """
    return {"statusCode": error.code,  "message": error.description}, \
        error.code if error.code is not None else StatusCode.BAD_REQUEST.value


def handle_application_error(error: Exception) -> Tuple[Dict[str, Any], int]:
    """
    Method handles all application errors.
    Args:
        error: Application error.

    Returns:
        tuple: Dictionary whit application error information and status code.
    """
    return {"statusCode": StatusCode.APPLICATION_ERROR.value,
            "errorCode": error.__class__.__name__,
            "message": "Internal Server Error."}, StatusCode.APPLICATION_ERROR.value