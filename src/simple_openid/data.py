"""
Datatypes and models for various OpenID messages
"""
import logging
from typing import List, Optional, Union

from pydantic import BaseModel, Extra, HttpUrl

from simple_openid.base_data import OpenidBaseModel, OpenidMessage

logger = logging.getLogger(__name__)


class ProviderMetadata(BaseModel):
    """
    OpenID Providers have metadata describing their configuration

    Additional OpenID Provider Metadata parameters MAY also be used. Some are defined by other specifications, such as `OpenID Connect Session Management 1.0 <https://openid.net/specs/openid-connect-session-1_0.html>`_.

    See `OpenID Connect Spec: Provider Metadata <https://openid.net/specs/openid-connect-discovery-1_0.html#ProviderMetadata>`_
    """

    class Config:
        extra = Extra.allow
        allow_mutation = False

    issuer: HttpUrl
    "REQUIRED. URL using the https scheme with no query or fragment component that the OP asserts as its Issuer Identifier This MUST be identical to the iss Claim value in ID Tokens issued from this Issuer."

    authorization_endpoint: HttpUrl
    "REQUIRED. URL of the OP's OAuth 2.0 Authorization Endpoint."

    token_endpoint: Optional[HttpUrl]
    "URL of the OP's OAuth 2.0 Token Endpoint. This is REQUIRED unless only the Implicit Flow is used."

    userinfo_endpoint: Optional[HttpUrl]
    "RECOMMENDED. URL of the OP's UserInfo Endpoint. This URL MUST use the https scheme and MAY contain port, path, and query parameter components."

    jwks_uri: HttpUrl
    "REQUIRED. URL of the OP's JSON Web Key Set document This contains the signing key(s) the RP uses to validate signatures from the OP The JWK Set MAY also contain the Server's encryption key(s), which are used by RPs to encrypt requests to the Server When both signing and encryption keys are made available, a use (Key Use) parameter value is REQUIRED for all keys in the referenced JWK Set to indicate each key's intended usage Although some algorithms allow the same key to be used for both signatures and encryption, doing so is NOT RECOMMENDED, as it is less secure The JWK x5c parameter MAY be used to provide X.509 representations of keys provided When used, the bare key values MUST still be present and MUST match those in the certificate. "

    registration_endpoint: Optional[HttpUrl]
    "RECOMMENDED. URL of the OP's Dynamic Client Registration Endpoint"

    scopes_supported: Optional[List[str]]
    "RECOMMENDED. JSON array containing a list of the OAuth 2.0 scope values that this server supports The server MUST support the openid scope value Servers MAY choose not to advertise some supported scope values even when this parameter is used, although those defined in SHOULD be listed, if supported."

    response_types_supported: Optional[List[str]]
    "REQUIRED. JSON array containing a list of the OAuth 2.0 response_type values that this OP supports Dynamic OpenID Providers MUST support the code, id_token, and the token id_token Response Type values."

    response_modes_supported: Optional[List[str]] = ["query", "fragment"]
    "OPTIONAL. JSON array containing a list of the OAuth 2.0 response_mode values that this OP supports, as specified in OAuth 2.0 Multiple Response Type Encoding Practices. " 'If omitted, the default for Dynamic OpenID Providers is ["query", "fragment"].'

    grant_types_supported: Optional[List[str]] = ["authorization_code", "implicit"]
    "OPTIONAL. JSON array containing a list of the OAuth 2.0 Grant Type values that this OP supports Dynamic OpenID Providers MUST support the authorization_code and implicit Grant Type values and MAY support other Grant Types. " 'If omitted, the default value is ["authorization_code", "implicit"].'

    acr_values_supported: Optional[List[str]]
    "OPTIONAL. JSON array containing a list of the Authentication Context Class References that this OP supports."

    subject_types_supported: List[str]
    "REQUIRED. JSON array containing a list of the Subject Identifier types that this OP supports Valid types include pairwise and public."

    id_token_signing_alg_values_supported: List[str]
    "REQUIRED. JSON array containing a list of the JWS signing algorithms (alg values) supported by the OP for the ID Token to encode the Claims in a JWT The algorithm RS256 MUST be included The value none MAY be supported, but MUST NOT be used unless the Response Type used returns no ID Token from the Authorization Endpoint (such as when using the Authorization Code Flow)."

    id_token_encryption_alg_values_supported: Optional[List[str]]
    "OPTIONAL. JSON array containing a list of the JWE encryption algorithms (alg values) supported by the OP for the ID Token to encode the Claims in a JWT."

    id_token_encryption_enc_values_supported: Optional[List[str]]
    "OPTIONAL. JSON array containing a list of the JWE encryption algorithms (enc values) supported by the OP for the ID Token to encode the Claims in a JWT."

    userinfo_signing_alg_values_supported: Optional[List[str]]
    "OPTIONAL. JSON array containing a list of the JWS signing algorithms (alg values) supported by the UserInfo Endpoint to encode the Claims in a JWT The value none MAY be included."

    userinfo_encryption_alg_values_supported: Optional[List[str]]
    "OPTIONAL. JSON array containing a list of the JWE encryption algorithms (alg values) supported by the UserInfo Endpoint to encode the Claims in a JWT."

    userinfo_encryption_enc_values_supported: Optional[List[str]]
    "OPTIONAL. JSON array containing a list of the JWE encryption algorithms (enc values) supported by the UserInfo Endpoint to encode the Claims in a JWT."

    request_object_signing_alg_values_supported: Optional[List[str]]
    "OPTIONAL. JSON array containing a list of the JWS signing algorithms (alg values) supported by the OP for Request Objects, which are described in Section 6.1 of OpenID Connect Core 1.0 These algorithms are used both when the Request Object is passed by value (using the request parameter) and when it is passed by reference (using the request_uri parameter) Servers SHOULD support none and RS256."

    request_object_encryption_alg_values_supported: Optional[List[str]]
    "OPTIONAL. JSON array containing a list of the JWE encryption algorithms (alg values) supported by the OP for Request Objects These algorithms are used both when the Request Object is passed by value and when it is passed by reference."

    request_object_encryption_enc_values_supported: Optional[List[str]]
    "OPTIONAL. JSON array containing a list of the JWE encryption algorithms (enc values) supported by the OP for Request Objects These algorithms are used both when the Request Object is passed by value and when it is passed by reference."

    token_endpoint_auth_methods_supported: Optional[List[str]] = ["client_secret_basic"]
    "OPTIONAL. JSON array containing a list of Client Authentication methods supported by this Token Endpoint The options are client_secret_post, client_secret_basic, client_secret_jwt, and private_key_jwt, as described in Section 9 of OpenID Connect Core 1.0 Other authentication methods MAY be defined by extensions. If omitted, the default is client_secret_basic -- the HTTP Basic Authentication Scheme specified in Section 2.3.1 of OAuth 2.0 [RFC6749]."

    token_endpoint_auth_signing_alg_values_supported: Optional[List[str]]
    "OPTIONAL. JSON array containing a list of the JWS signing algorithms (alg values) supported by the Token Endpoint for the signature on the JWT used to authenticate the Client at the Token Endpoint for the private_key_jwt and client_secret_jwt authentication methods Servers SHOULD support RS256 The value none MUST NOT be used."

    display_values_supported: Optional[List[str]]
    "OPTIONAL. JSON array containing a list of the display parameter values that the OpenID Provider supports These values are described in Section 3.1.2.1 of OpenID Connect Core 1.0."

    claim_types_supported: Optional[List[str]]
    "OPTIONAL. JSON array containing a list of the Claim Types that the OpenID Provider supports These Claim Types are described in Section 5.6 of OpenID Connect Core 1.0 Values defined by this specification are normal, aggregated, and distributed If omitted, the implementation supports only normal Claims."

    claims_supported: Optional[List[str]]
    "RECOMMENDED. JSON array containing a list of the Claim Names of the Claims that the OpenID Provider MAY be able to supply values for Note that for privacy or other reasons, this might not be an exhaustive list."

    service_documentation: Optional[HttpUrl]
    "OPTIONAL. URL of a page containing human-readable information that developers might want or need to know when using the OpenID Provider In particular, if the OpenID Provider does not support Dynamic Client Registration, then information on how to register Clients needs to be provided in this documentation."

    claims_locales_supported: Optional[List[str]]
    "OPTIONAL. Languages and scripts supported for values in Claims being returned, represented as a JSON array of BCP47 [RFC5646] language tag values Not all languages and scripts are necessarily supported for all Claim values."

    ui_locales_supported: Optional[List[str]]
    "OPTIONAL. Languages and scripts supported for the user interface, represented as a JSON array of BCP47 [RFC5646] language tag values."

    claims_parameter_supported: Optional[bool] = False
    "OPTIONAL. Boolean value specifying whether the OP supports use of the claims parameter, with true indicating support If omitted, the default value is false."

    request_parameter_supported: Optional[bool] = False
    "OPTIONAL. Boolean value specifying whether the OP supports use of the request parameter, with true indicating support If omitted, the default value is false."

    request_uri_parameter_supported: Optional[bool] = True
    "OPTIONAL. Boolean value specifying whether the OP supports use of the request_uri parameter, with true indicating support. If omitted, the default value is true."

    require_request_uri_registration: Optional[bool] = False
    "OPTIONAL. Boolean value specifying whether the OP requires any request_uri values used to be pre-registered using the request_uris registration parameter Pre-registration is REQUIRED when the value is true. If omitted, the default value is false."

    op_policy_uri: Optional[HttpUrl]
    "OPTIONAL. URL that the OpenID Provider provides to the person registering the Client to read about the OP's requirements on how the Relying Party can use the data provided by the OP The registration process SHOULD display this URL to the person registering the Client if it is given."

    op_tos_uri: Optional[HttpUrl]
    "OPTIONAL. URL that the OpenID Provider provides to the person registering the Client to read about OpenID Provider's terms of service The registration process SHOULD display this URL to the person registering the Client if it is given. "


class IdToken(OpenidBaseModel):
    """
    The primary extension that OpenID Connect makes to OAuth 2.0 to enable End-Users to be Authenticated is this ID Token data structure.
    The ID Token is a security token that contains Claims about the Authentication of an End-User by an Authorization Server when using a Client, and potentially other requested Claims.

    ID tokens may contain more claims which may be present in this object.

    See `Section 2 of OpenID Connect Core 1.0 <https://openid.net/specs/openid-connect-core-1_0.html#IDToken>`_
    """

    class Config:
        extra = Extra.allow
        allow_mutation = False

    iss: HttpUrl
    "REQUIRED. Issuer Identifier for the Issuer of the response The iss value is a case sensitive URL using the https scheme that contains scheme, host, and optionally, port number and path components and no query or fragment components."

    sub: str
    "REQUIRED. Subject Identifier A locally unique and never reassigned identifier within the Issuer for the End-User, which is intended to be consumed by the Client, e.g., 24400320 or AItOawmwtWwcT0k51BayewNvutrJUqsvl6qs7A4 It MUST NOT exceed 255 ASCII characters in length The sub value is a case sensitive string."

    aud: Union[str, List[str]]
    "REQUIRED. Audience(s) that this ID Token is intended for It MUST contain the OAuth 2.0 client_id of the Relying Party as an audience value It MAY also contain identifiers for other audiences In the general case, the aud value is an array of case sensitive strings In the common special case when there is one audience, the aud value MAY be a single case sensitive string."

    exp: int
    "REQUIRED. Expiration time on or after which the ID Token MUST NOT be accepted for processing The processing of this parameter requires that the current date/time MUST be before the expiration date/time listed in the value Implementers MAY provide for some small leeway, usually no more than a few minutes, to account for clock skew Its value is a JSON number representing the number of seconds from 1970-01-01T0:0:0Z as measured in UTC until the date/time."

    iat: int
    "REQUIRED. Time at which the JWT was issued Its value is a JSON number representing the number of seconds from 1970-01-01T0:0:0Z as measured in UTC until the date/time."

    auth_time: Optional[int]
    "Time when the End-User authentication occurred Its value is a JSON number representing the number of seconds from 1970-01-01T0:0:0Z as measured in UTC until the date/time When a max_age request is made or when auth_time is requested as an Essential Claim, then this Claim is REQUIRED; otherwise, its inclusion is OPTIONAL (The auth_time Claim semantically corresponds to the OpenID 2.0 PAPE [OpenID.PAPE] auth_time response parameter.)"

    nonce: Optional[str]
    "String value used to associate a Client session with an ID Token, and to mitigate replay attacks The value is passed through unmodified from the Authentication Request to the ID Token If present in the ID Token, Clients MUST verify that the nonce Claim Value is equal to the value of the nonce parameter sent in the Authentication Request If present in the Authentication Request, Authorization Servers MUST include a nonce Claim in the ID Token with the Claim Value being the nonce value sent in the Authentication Request Authorization Servers SHOULD perform no other processing on nonce values used The nonce value is a case sensitive string. "

    acr: Optional[str]
    "OPTIONAL. Authentication Context Class Reference String specifying an Authentication Context Class Reference value that identifies the Authentication Context Class that the authentication performed satisfied. " 'The value "0" indicates the End-User authentication did not meet the requirements of ISO/IEC 29115 [ISO29115] level 1. ' 'Authentication using a long-lived browser cookie, for instance, is one example where the use of "level 0" is appropriate. ' "Authentications with level 0 SHOULD NOT be used to authorize access to any resource of any monetary value (This corresponds to the OpenID 2.0 PAPE [OpenID.PAPE] nist_auth_level 0.)  An absolute URI or an RFC 6711 [RFC6711] registered name SHOULD be used as the acr value; registered names MUST NOT be used with a different meaning than that which is registered Parties using this claim will need to agree upon the meanings of the values used, which may be context-specific The acr value is a case sensitive string."

    amr: Optional[List[str]]
    "OPTIONAL. Authentication Methods References JSON array of strings that are identifiers for authentication methods used in the authentication For instance, values might indicate that both password and OTP authentication methods were used The definition of particular values to be used in the amr Claim is beyond the scope of this specification Parties using this claim will need to agree upon the meanings of the values used, which may be context-specific The amr value is an array of case sensitive strings."

    azp: Optional[str]
    "OPTIONAL. Authorized party - the party to which the ID Token was issued If present, it MUST contain the OAuth 2.0 Client ID of this party This Claim is only needed when the ID Token has a single audience value and that audience is different than the authorized party It MAY be included even when the authorized party is the same as the sole audience The azp value is a case sensitive string containing a StringOrURI value."


class UserinfoRequest(OpenidMessage):
    pass


class UserinfoSuccessResponse(OpenidMessage):
    class Config:
        extra = Extra.allow
        allow_mutation = False

    sub: str


class UserinfoErrorResponse(OpenidMessage):
    class Config:
        allow_mutation = False

    error: str
    error_description: Optional[str]


import enum
from typing import List, Optional

from pydantic import Extra

from simple_openid.data import OpenidMessage


class AuthenticationRequest(OpenidMessage):
    """
    An Authentication Request requests that the End-User be authenticated by the Authorization Server.
    """

    class Config:
        extra = Extra.allow

    scope: str
    "REQUIRED. OpenID Connect authentication requests MUST contain the openid scope value. Multiple scopes are encoded space separated If the openid scope value is not present, the behavior is entirely unspecified Other scope values MAY be present."

    response_type: str
    "REQUIRED. OAuth 2.0 Response Type value that determines the authorization processing flow to be used, including what parameters are returned from the endpoints used When using the Authorization Code Flow, this value is code. "

    client_id: str
    "REQUIRED. OAuth 2.0 Client Identifier valid at the Authorization Server."

    redirect_uri: str
    "REQUIRED. Redirection URI to which the response will be sent This URI MUST exactly match one of the Redirection URI values for the Client pre-registered at the OpenID Provider When using this flow, the Redirection URI SHOULD use the https scheme; however, it MAY use the http scheme, provided that the Client Type is confidential, as defined in Section 2.1 of OAuth 2.0, and provided the OP allows the use of http Redirection URIs in this case The Redirection URI MAY use an alternate scheme, such as one that is intended to identify a callback into a native application."

    state: Optional[str]
    "RECOMMENDED. Opaque value used to maintain state between the request and the callback Typically, Cross-Site Request Forgery (CSRF, XSRF) mitigation is done by cryptographically binding the value of this parameter with a browser cookie."

    response_mode: Optional[str]
    "OPTIONAL. Informs the Authorization Server of the mechanism to be used for returning parameters from the Authorization Endpoint. This use of this parameter is NOT RECOMMENDED when the Response Mode that would be requested is the default mode specified for the Response Type."

    nonce: Optional[str]
    "OPTIONAL. String value used to associate a Client session with an ID Token, and to mitigate replay attacks The value is passed through unmodified from the Authentication Request to the ID Token Sufficient entropy MUST be present in the nonce values used to prevent attackers from guessing values."

    display: Optional[List[str]]
    'OPTIONAL. Space delimited, case sensitive list of ASCII string values that specifies whether the Authorization Server prompts the End-User for reauthentication and consent. The defined values are: "page", "popup", "touch" and "wap"'

    prompt: Optional[List[str]]
    'OPTIONAL. Space delimited, case sensitive list of ASCII string values that specifies whether the Authorization Server prompts the End-User for reauthentication and consent. The defined values are: "none", "login", "consent" and "select_account".'

    max_age: Optional[int]
    "OPTIONAL. Maximum Authentication Age Specifies the allowable elapsed time in seconds since the last time the End-User was actively authenticated by the OP If the elapsed time is greater than this value, the OP MUST attempt to actively re-authenticate the End-User When max_age is used, the ID Token returned MUST include an auth_time Claim Value."

    ui_locales: Optional[List[str]]
    "OPTIONAL. End-User's preferred languages and scripts for the user interface, represented as a space-separated list of BCP47 [RFC5646] language tag values, ordered by preference. " 'For instance, the value "fr-CA fr en" represents a preference for French as spoken in Canada, then French (without a region designation), followed by English (without a region designation). ' "An error SHOULD NOT result if some or all of the requested locales are not supported by the OpenID Provider."

    id_token_hint: Optional[str]
    "OPTIONAL. ID Token previously issued by the Authorization Server being passed as a hint about the End-User's current or past authenticated session with the Client If the End-User identified by the ID Token is logged in or is logged in by the request, then the Authorization Server returns a positive response; otherwise, it SHOULD return an error, such as login_required When possible, an id_token_hint SHOULD be present when prompt=none is used and an invalid_request error MAY be returned if it is not; however, the server SHOULD respond successfully when possible, even if it is not present The Authorization Server need not be listed as an audience of the ID Token when it is used as an id_token_hint value. "

    login_hint: Optional[str]
    "OPTIONAL. Hint to the Authorization Server about the login identifier the End-User might use to log in (if necessary) This hint can be used by an RP if it first asks the End-User for their e-mail address (or other identifier) and then wants to pass that value as a hint to the discovered authorization service It is RECOMMENDED that the hint value match the value used for discovery (which is not supported by this library) This value MAY also be a phone number in the format specified for the `phone_number` Claim The use of this parameter is left to the OP's discretion."

    acr_values: Optional[List[str]]
    "OPTIONAL. Requested Authentication Context Class Reference values Space-separated string that specifies the acr values that the Authorization Server is being requested to use for processing this Authentication Request, with the values appearing in order of preference The Authentication Context Class satisfied by the authentication performed is returned as the acr Claim Value, as specified in Section 2 The acr Claim is requested as a Voluntary Claim by this parameter."


class AuthenticationSuccessResponse(OpenidMessage):
    """
    A response that is sent by the Authorization Server if a previous :class:`.AuthenticationRequest` could successfully
    be parsed and handled.

    When using the Authorization Code Flow (this flow), the Authorization Response MUST return the parameters defined by adding them as query parameters to the redirect_uri specified in the Authorization Request using the application/x-www-form-urlencoded format, unless a different Response Mode was specified.
    """

    class Config:
        allow_mutation = False

    code: str
    "REQUIRED. The authorization code generated by the authorization server The authorization code MUST expire shortly after it is issued to mitigate the risk of leaks A maximum authorization code lifetime of 10 minutes is RECOMMENDED The client MUST NOT use the authorization code more than once If an authorization code is used more than once, the authorization server MUST deny the request and SHOULD revoke (when possible) all tokens previously issued based on that authorization code The authorization code is bound to the client identifier and redirect URI."

    state: Optional[str]
    "REQUIRED if the `state` parameter was present in the client authorization request The exact value received from the client."


class AuthenticationErrorResponse(OpenidMessage):
    """
    A response that is sent by the Authorization Server if a previous :class:`.AuthenticationRequest` could not be
    understood or handled.
    It contains additional information about the error that occurred.

    If the End-User denies the request or the End-User authentication fails, the OP (Authorization Server) informs the RP (Client) by using the Error Response parameters.
    (General HTTP errors are returned to the User Agent using the appropriate HTTP status code.)
    """

    class Config:
        extra = Extra.allow
        allow_mutation = False
        use_enum_values = True

    class ErrorType(enum.Enum):
        """
        Possible values for :data:`error <AuthenticationErrorResponse.error>`
        """

        invalid_request = "invalid_request"
        "The request is missing a required parameter, includes an invalid parameter value, includes a parameter more than once, or is otherwise malformed."

        unauthorized_client = "unauthorized_client"
        "The client is not authorized to request an authorization code using this method."

        access_denied = "access_denied"
        "The resource owner or authorization server denied the request."

        unsupported_response_type = "unsupported_response_type"
        "The authorization server does not support obtaining an authorization code using this method."

        invalid_scope = "invalid_scope"
        "The requested scope is invalid, unknown, or malformed."

        server_error = "server_error"
        "The authorization server encountered an unexpected condition that prevented it from fulfilling the request (This error code is needed because a 500 Internal Server Error HTTP status code cannot be returned to the client via an HTTP redirect.)"

        temporarily_unavailable = "temporarily_unavailable"
        "The authorization server is currently unable to handle the request due to a temporary overloading or maintenance of the server (This error code is needed because a 503 Service Unavailable HTTP status code cannot be returned to the client via an HTTP redirect.)"

        interaction_required = "interaction_required"
        "The Authorization Server requires End-User interaction of some form to proceed This error MAY be returned when the prompt parameter value in the Authentication Request is none, but the Authentication Request cannot be completed without displaying a user interface for End-User interaction."

        login_required = "login_required"
        "The Authorization Server requires End-User authentication This error MAY be returned when the prompt parameter value in the Authentication Request is none, but the Authentication Request cannot be completed without displaying a user interface for End-User authentication."

        account_selection_required = "account_selection_required"
        "The End-User is REQUIRED to select a session at the Authorization Server The End-User MAY be authenticated at the Authorization Server with different associated accounts, but the End-User did not select a session This error MAY be returned when the prompt parameter value in the Authentication Request is none, but the Authentication Request cannot be completed without displaying a user interface to prompt for a session to use."

        consent_required = "consent_required"
        "The Authorization Server requires End-User consent This error MAY be returned when the prompt parameter value in the Authentication Request is none, but the Authentication Request cannot be completed without displaying a user interface for End-User consent."

        invalid_request_uri = "invalid_request_uri"
        "The `request_uri` in the Authorization Request returns an error or contains invalid data."

        invalid_request_object = "invalid_request_object"
        "The request parameter contains an invalid Request Object."

        request_not_supported = "request_not_supported"
        "The OP does not support use of the request parameter."

        request_uri_not_supported = "request_uri_not_supported"
        "The OP does not support use of the request_uri parameter."

        registration_not_supported = "registration_not_supported"
        "The OP does not support use of the registration parameter."

    error: ErrorType
    "REQUIRED.  An error code"

    error_description: Optional[str]
    "OPTIONAL. Human-readable text providing additional information, used to assist the client developer in understanding the error that occurred."

    error_uri: Optional[str]
    "OPTIONAL. A URI identifying a human-readable web page with information about the error, used to provide the client developer with additional information about the error."

    state: Optional[str]
    "REQUIRED if a `state` parameter was present in the client authorization request. The exact value received from the client."


class TokenRequest(OpenidMessage):
    """
    A Client makes a Token Request by presenting its Authorization Grant (in the form of an Authorization Code) to the Token Endpoint.
    If the Client is a Confidential Client, then it MUST authenticate to the Token Endpoint using the authentication method registered for its client_id.

    This request MUST be sent to the token endpoint using POST with "application/x-www-form-urlencoded" body.
    """

    class Config:
        extra = Extra.allow

    grant_type: str
    'REQUIRED. Value MUST be set to "authorization_code".'

    code: str
    "REQUIRED. The authorization code received from the authorization server."

    redirect_uri: str
    "REQUIRED, must be identical to the value that was included in the :data:`AuthenticationRequest <AuthenticationRequest.redirect_uri>`."

    client_id: Optional[str]
    "REQUIRED, if the client is not authenticating with the authorization server. Basically, confidential clients don't need to include it but others do."


class TokenSuccessResponse(OpenidMessage):
    """
    After receiving and validating a valid and authorized :class:`TokenRequest <TokenRequest>` from the Client, the Authorization Server returns a successful response that includes an ID Token and an Access Token
    """

    # TODO Implement ID Token validation
    # https://openid.net/specs/openid-connect-core-1_0.html#IDTokenValidation

    class Config:
        allow_mutation = False

    access_token: str
    "REQUIRED. The access token issued by the authorization server."

    token_type: str
    "REQUIRED. The type of the token issued Value is case insensitive. Usually this is `Bearer` which is a type that MUST be supported by all OPs."

    expires_in: Optional[int]
    'RECOMMENDED.  The lifetime in seconds of the access token. For example, the value "3600" denotes that the access token will expire in one hour from the time the response was generated. If omitted, the authorization server SHOULD provide the expiration time via other means or document the default value.'

    refresh_token: Optional[str]
    "OPTIONAL. The refresh token, which can be used to obtain new access tokens using the same authorization grant as described in `Section 6 of RFC6749 <https://www.rfc-editor.org/rfc/rfc6749#section-6>`_."

    scope: Optional[str]
    "OPTIONAL, if identical to the scope requested by the client; otherwise, REQUIRED. The scope of the access token."

    id_token: str
    "ID Token value associated with the authenticated session."


class TokenErrorResponse(OpenidMessage):
    """
    A response that is sent by the Authorization Server if a previous :class:`.TokenRequest` could not be
    understood or handled.
    It contains additional information about the error that occurred.
    """

    class Config:
        extra = Extra.allow
        allow_mutation = False
        use_enum_values = True

    class ErrorType(enum.Enum):
        """
        Possible values for :data:`error <TokenErrorResponse.error>`
        """

        invalid_request = "invalid_request"
        "The request is missing a required parameter, includes an unsupported parameter value (other than grant type), repeats a parameter, includes multiple credentials, utilizes more than one mechanism for authenticating the client, or is otherwise malformed."

        invalid_client = "invalid_client"
        "Client authentication failed (e.g., unknown client, no client authentication included, or unsupported authentication method). The authorization server MAY return an HTTP 401 (Unauthorized) status code to indicate which HTTP authentication schemes are supported. " 'If the client attempted to authenticate via the "Authorization" request header field, the authorization server MUST respond with an HTTP 401 (Unauthorized) status code and include the "WWW-Authenticate" response header field matching the authentication scheme used by the client.'

        invalid_grant = "invalid_grant"
        "The provided authorization grant (e.g., authorization code, resource owner credentials) or refresh token is invalid, expired, revoked, does not match the redirection URI used in the authorization request, or was issued to another client."

        unauthorized_client = "unauthorized_client"
        "The authenticated client is not authorized to use this authorization grant type."

        unsupported_grant_type = "unsupported_grant_type"
        "The authorization grant type is not supported by the authorization server."

        invalid_scope = "invalid_scope"
        "The requested scope is invalid, unknown, malformed, or exceeds the scope granted by the resource owner."

    error: ErrorType
    "REQUIRED. An error code"

    error_description: Optional[str]
    "OPTIONAL.  Human-readable text providing additional information, used to assist the client developer in understanding the error that occurred."

    error_uri: Optional[str]
    "OPTIONAL.  A URI identifying a human-readable web page with information about the error, used to provide the client developer with additional information about the error."
