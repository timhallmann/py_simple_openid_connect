"""
Internal utilities
"""

from simple_openid_connect.exceptions import ValidationError


def is_application_json(content_type: str) -> bool:
    """
    Whether the given content type is `application/json`.
    This is needed because mime types can contain additional options which are ignored here.
    """
    main_type = _parse_header(content_type)
    return main_type == "application/json"


def validate_that(condition: bool, msg: str) -> None:
    """
    Validate that the given condition is true, raising a ValidationError with the given message if it is not.

    This is implemented to write concise validating assertions.

    :raises ValidationError: if the condition is false
    """
    if not condition:
        raise ValidationError(msg)


def _parse_header(line):
    """Parse a Content-type like header.

    Return the main content-type and a dictionary of options.
    """
    # Adapted from https://github.com/python/cpython/blob/3.12/Lib/cgi.py
    return _parseparam(";" + line).__next__()


def _parseparam(s):
    # Copied from https://github.com/python/cpython/blob/3.12/Lib/cgi.py
    while s[:1] == ";":
        s = s[1:]
        end = s.find(";")
        while end > 0 and (s.count('"', 0, end) - s.count('\\"', 0, end)) % 2:
            end = s.find(";", end + 1)
        if end < 0:
            end = len(s)
        f = s[:end]
        yield f.strip()
        s = s[end:]
