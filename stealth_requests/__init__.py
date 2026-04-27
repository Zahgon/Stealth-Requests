from functools import partial

from .session import StealthSession, AsyncStealthSession
from .response import StealthResponse

from curl_cffi.requests.session import HttpMethod


def request(method: HttpMethod, url: str, *args, **kwargs) -> StealthResponse:
    pass


head = partial(request, 'HEAD')
get = partial(request, 'GET')
post = partial(request, 'POST')
put = partial(request, 'PUT')
patch = partial(request, 'PATCH')
delete = partial(request, 'DELETE')
options = partial(request, 'OPTIONS')
