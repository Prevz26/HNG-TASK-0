from typing import Optional, Tuple, Dict, Any


NOT_FOUND = "Not found!"
SUCCESS = "Success"
SERVER_ERROR = "An error occurred on the server"

class CustomResponse:
    """Custom response class for consistent API responses"""

    def _create_response(
        self,
        # status: str,
        # message: str,
        data: Optional[Any] = None,
        status_code: int = 200
    ) -> Tuple[Dict[str, Any], int]:
        """
        Create a standardized response format.

        Args:
            status (str): Response status ('success' or 'error')
            message (str): Response message
            data (Any, optional): Response data
            status_code (int): HTTP status code

        Returns:
            Tuple[Dict[str, Any], int]: Response dict and status code
        """
        response = {
            # 'status': status,
            # 'message': message,
            'data': data,
        }
        return response, status_code

    def success_response(
        self,
        # message: str = SUCCESS,
        data: Optional[Any] = None,
        status_code: int = 200,
    ) -> Tuple[Dict[str, Any], int]:
        """Create a success response"""
        return self._create_response( data, status_code)

    def error_response(
        self,
        message: str,
        status_code: int,
        data: Optional[Any] = None
    ) -> Tuple[Dict[str, Any], int]:
        """Create an error response"""
        return self._create_response('error', message, data, status_code)
custom_response = CustomResponse()