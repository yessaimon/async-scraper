class ScraperError(Exception):
    pass


class HTTPError(ScraperError):
    pass


class SecurityError(ScraperError):
    pass
