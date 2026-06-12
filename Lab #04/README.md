# Signature is validated
## Asymmetric alg is used to sign
### Trying to bypass the authentication by injecting jwk key in the header
JWT header example:
```
{
    "kid": "ed2Nf8sb-sD6ng0-scs5390g-fFD8sfxG",
    "typ": "JWT",
    "alg": "RS256",
    "jwk": {
        "kty": "RSA",
        "e": "AQAB",
        "kid": "ed2Nf8sb-sD6ng0-scs5390g-fFD8sfxG",
        "n": "yy1wpYmffgXBxhAUJzHHocCuJolwDqql75ZWuCQ_cb33K2vh9m"
    }
}
```
jwk value represents the public key as json
### Server in this case trusts any public key provided in the jwk value when it should have only trust a whitelist of public keys 