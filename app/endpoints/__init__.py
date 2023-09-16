from app.endpoints.auth import api as auth_api
from app.endpoints.account import api as account_api


routes = [
    auth_api,
    account_api,
]

__all__ = ['routes']