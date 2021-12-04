class Unauthorized(Exception):
    """Exception: Represent error class for response status code 401. This mean you are unauthorized."""
    def __init__(self):
        super().__init__("Request return an Exception (code: 401): You are not authorize to do this request!")


class TooManyRequests(Exception):
    """Exception: Represent error class for response status code 429. This mean you made too much requests."""
    def __init__(self):
        super().__init__("Request return an Exception (code: 429): Ratelimit exceeded! You made too much requests, please wait couple of minutes!")

class InternalServerError(Exception):
    """Exception: Represent error class for response status code 500. This can mean many things, one of them is invalid image passed in image manipulation endpoint."""
    def __init__(self):
        super().__init__("Request return an Exception (code: 500): Invalid image passed.")