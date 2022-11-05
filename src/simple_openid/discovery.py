"""
Mechanisms for discovering information about an OpenID issuer
"""
import requests

from simple_openid.data import ProviderMetadata
from simple_openid.exceptions import OpenidProtocolError


def discover_configuration_from_issuer(issuer: str) -> ProviderMetadata:
    """
    Retrieve configuration information about an OpenID provider (issuer)

    For more information about this process see `Section 4 of OpenID Connect Discovery 1.0 <https://openid.net/specs/openid-connect-discovery-1_0.html#ProviderConfig>`_.

    :param issuer: The base url of the provider
        This url will be appended with `/.well-known/openid-configuration` to retrieve the provider configuration so
        that must be a valid URL for your provider.
    :returns: The well-formed and validated configuration of the given issuer
    :raises OpenidProtocolError: When the communication with the provider was not possible or the response was not in an
        expected format
    """
    issuer = issuer.removesuffix("/")
    response = requests.get(f"{issuer}/.well-known/openid-configuration")

    if response.headers.get("Content-Type") != "application/json":
        raise OpenidProtocolError(
            "The provider did not respond with a json document although it is required to do so",
            response.headers.get("Content-Type"),
        )

    try:
        result = ProviderMetadata.parse_raw(response.content)
        assert result.issuer == issuer
    except Exception as e:
        raise OpenidProtocolError(
            "The provider did not respond with a provider configuration according to spec"
        ) from e

    return result
