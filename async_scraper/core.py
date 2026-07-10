import aiohttp
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import ipaddress
import socket


from .cache import get, set
from .exceptions import (
    HTTPError,
    SecurityError
)


_session = None


DEFAULT_HEADERS = {

    "User-Agent":
    "Mozilla/5.0 (Android 15) "
    "AppleWebKit/537.36 "
    "Chrome/120 Safari/537.36",

    "Accept":
    "text/html,application/xhtml+xml",

    "Accept-Language":
    "ru,en;q=0.9"
}


MAX_SIZE = 5 * 1024 * 1024



async def _session_get():

    global _session


    if _session is None or _session.closed:

        timeout = aiohttp.ClientTimeout(
            total=15
        )


        connector = aiohttp.TCPConnector(
            limit=20
        )


        _session = aiohttp.ClientSession(
            headers=DEFAULT_HEADERS,
            timeout=timeout,
            connector=connector
        )


    return _session



def _check_url(url):

    parsed = urlparse(url)


    if parsed.scheme not in (
        "http",
        "https"
    ):
        raise SecurityError(
            "Only http/https allowed"
        )


    host = parsed.hostname


    if host:

        try:

            ip = socket.gethostbyname(
                host
            )


            if ipaddress.ip_address(ip).is_private:

                raise SecurityError(
                    "Private IP blocked"
                )


        except ValueError:
            pass



async def fetch(
    url: str,
    selector: str,
    attr: str = "text",
    cache=True,
    ttl=300
):


    _check_url(url)


    key = (
        url,
        selector,
        attr
    )


    if cache:

        saved = get(key)

        if saved is not None:
            return saved



    session = await _session_get()



    async with session.get(url) as response:


        if response.status != 200:

            raise HTTPError(
                f"HTTP {response.status}"
            )


        size = response.headers.get(
            "Content-Length"
        )


        if size and int(size) > MAX_SIZE:

            raise HTTPError(
                "Response too large"
            )


        html = await response.text()



    soup = BeautifulSoup(
        html,
        "html.parser"
    )



    element = soup.select_one(
        selector
    )


    if not element:

        result = None


    elif attr == "text":

        result = element.get_text(
            strip=True
        )


    else:

        result = element.get(
            attr
        )



    if cache:

        set(
            key,
            result,
            ttl
        )


    return result




async def close():

    global _session


    if _session:

        await _session.close()

        _session = None
