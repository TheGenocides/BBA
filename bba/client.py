import requests
import json
from typing import Optional

from .objects import ResponseObject
from .errors import Unauthorized, TooManyRequests, InternalServerError


class Client:
    """Represent the client that make the request.

    Parameters
    ------------
    api_key: str
        The api key, the unique identifier used to connect to or perform an API call. You can get the key from here: https://api.breadbot.me/login 
    
    """
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.breadbot.me/"
        self.calc = self.calculator #alias

    def check_error(self, response: requests.models.Response):
        code = response.status_code
        if code == 401:
            raise Unauthorized()

        elif code == 429:
            raise TooManyRequests()

        elif code == 500:
            raise InternalServerError()

    def request(self, method: str, version: str, path: str, *, params: dict = {}, headers: dict = {}):
        url = self.base_url + version + path
        res = getattr(requests, method.lower(), None)
        if not res:
            raise TypeError("Wrong method argument passed!")

        if not headers:
            headers['api-key'] = self.api_key

        response = res(url, headers=headers, params=params)
        self.check_error(response)
        res = None
        try:
            res=response.json()
        except json.decoder.JSONDecodeError:
            return response

        return res

    def calculator(self, expression: str, ans: str = None) -> ResponseObject:
        """ResponseObject: Solve certain math equations.

        Parameters
        -----------
        expression: str:
            The math expression, e.g '6+6'
        ans: str:
            Filled the 'Ans' word in expression. e.g if expression is 'Ans+2+1' and you defined ans argument as 1. Then the expression change to: 1+2+1 which is 4.
    
        
        Docs
        ------
        https://api.breadbot.me/#calcPost
        """
        params={}

        if expression:
            params['calc'] = expression

        if ans:
            params['ans'] = ans

        res = self.request(
            "POST", 
            "v1",
            "/calc", 
            params=params
        )

        return ResponseObject(res)

    def get_sentence(self) -> ResponseObject:
        """ResponseObject: Generate a random sentence.
        
        Docs
        ------
        https://docs.api.breadbot.me/reference/api-reference/sentence-generator
        """
        res = self.request(
            "POST", 
            "v1", 
            "/sentence"
        )

        return ResponseObject(res)

    def invert_image(self, url: Optional[str] = None) -> Optional[bytes]:
        """Optional[:class:`bytes`]: Invert an image using the image url.

        Parameters
        ------------
        url: Optional[:class:`str`]
            The image's url to be invert.
        
        Docs
        ------
        https://docs.api.breadbot.me/reference/api-reference/image-manipulation
        """
        if not url:
            raise TypeError("Url cannot be None or empty string!")

        res = self.request(
            "POST",
            "v1",
            "/image/invert",
            params = {
                "img": url
            }
        )
        return res.content

    def pixelate_image(self, url: Optional[str] = None) -> Optional[bytes]:
        """Optional[:class:`bytes`]: Pixelate an image using the image url.

        Parameters
        ------------
        url: Optional[:class:`str`]
            The image's url to be pixelate.
        
        Docs
        ------
        https://docs.api.breadbot.me/reference/api-reference/image-manipulation
        """
        if not url:
            raise TypeError("Url cannot be None or empty string!")

        res = self.request(
            "POST",
            "v1",
            "/image/pixelate",
            params = {
                "img": url
            }
        )
        return res.content