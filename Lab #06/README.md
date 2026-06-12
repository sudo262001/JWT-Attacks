# Signature is validated
## Symmetric alg is used to sign
###  Verification keys are often stored as a JWK Set. In this case, the server may simply look for the JWK with the same kid as the token. However, the JWS specification doesn't define a concrete structure for this ID - it's just an arbitrary string of the developer's choosing. For example, they might use the kid parameter to point to a particular entry in a database, or even the name of a file.
* Test if this parameter is also vulnerable to directory traversal

AA== is the base64 encoding of the null string which is what the server gets when trying to get the key from /dev/null 