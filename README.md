# JWT-Attacks
PortSwigger Labs

# General Notes!!
- Even if the token is unsigned, the payload part must still be terminated with a trailing dot.

# Testing Scenarios

## 1. Sensitive information encoded in payload
## 2. JWT stored in insecure locations
- Insecure cookie: No HTTPOnly flag, No Security flag
- Stored in local storage
## 3. Expiration never checked or active for so long
## 4. Signature is not verified
arbitrary signatures is never checked, the root cause is when developers miss that decoding the request and extracting the token is not enough they also need to verify it
## 5. none algorithm is allowed
## 6. Weak/Guessable key (symmetric)
## 7. Header injection via jwk parameter
## 8. Header injection via jku parameter
## 9. Header injection via kid parameter

## Other interesting JWT header parameters
The following header parameters may also be interesting for attackers:

    cty (Content Type) 
    - Sometimes used to declare a media type for the content in the JWT payload. This is usually omitted from the header, but the underlying parsing library may support it anyway. 
    If you have found a way to bypass signature verification, you can try injecting a cty header to change the content type to text/xml or application/x-java-serialized-object, which can potentially enable new vectors for XXE and deserialization attacks.

    x5c (X.509 Certificate Chain) 
    - Sometimes used to pass the X.509 public key certificate or certificate chain of the key used to digitally sign the JWT. This header parameter can be used to inject self-signed certificates, similar to the jwk header injection attacks discussed above. 
    Due to the complexity of the X.509 format and its extensions, parsing these certificates can also introduce vulnerabilities. Details of these attacks are beyond the scope of these materials, but for more details, check out CVE-2017-2800 and CVE-2018-2633.
