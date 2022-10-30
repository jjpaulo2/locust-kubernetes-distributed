from os import environ
from typing import Tuple


class Auth:
    USER = environ.get('BASIC_AUTH_USER', 'admin')
    PASSWORD = environ.get('BASIC_AUTH_PASSWORD', '123')
    
    @classmethod
    def basic(cls) -> Tuple[str, str]:
        return (cls.USER, cls.PASSWORD)
        