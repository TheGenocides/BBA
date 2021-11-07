import requests
import json
from typing import Optional
from .objects import ResponseObject
from .errors import Unauthorized, TooManyRequests


class Client:
    """Represent the client that make the request.

    Parameters
    ------------
    api_key: str
        The api key, the unique identifier used to connect to or perform an API call. You can get the key from here: https://api.breadbot.me/login 
    
    """
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.breadbot.me"
        self.calc = self.calculator #alias

    def check_error(self, response: requests.models.Response):
        code = response.status_code
        if code == 401:
            raise Unauthorized()

        elif code == 429:
            raise TooManyRequests()

    def request(self, method: str, path: str, *, params: dict = {}, headers: dict = {}):
        url: str = self.base_url + path
        res: Optional[str] = getattr(requests, method.lower(), None)
        if not res:
            raise TypeError("Wrong method argument passed!")

        if not headers:
            headers['api-key'] = self.api_key

        response = res(url, headers=headers, params=params)
        self.check_error(response)
        print(response.text)
        res=response.json()

        return res

    def calculator(self, calc: str, ans: str = None) -> ResponseObject:
        """ResponseObject: Solve certain math equations (calcPost)

        Paramaters
        -----------
        calc: str:
            Equation of the math problem in string, e.g '1+5'

        ans: str:
            You can use this as a variable, e.g Ans+4
    
        
        Docs
        ------
        https://api.breadbot.me/#calcPost
        """
        params={}

        if calc:
            params['calc'] = calc

        if ans:
            params['ans'] = ans

        res = self.request(
            "POST", 
            "/calc", 
            params=params
        )

        return CalcObject(res)