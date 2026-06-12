# Signature is validated
## Asymmetric alg is used to sign
## Testing the server's respond when changing the algorithm to symmetric and sign with the asymmetric public key as the symmetric key
- public key can be obtained from an endpoint for ex: /jwks.json
- Extract 
```
{"kty":"RSA","e":"AQAB","use":"sig","kid":"b7454d0f-6d3c-47f8-ab47-fbef34a27d52","alg":"RS256","n":"xLVLxSM2lSQMTSf3Jx-GWIc6jvnUeCreN-4AT7jql38uyUpfuQ8yA-pkFuIm_3eMGOT8_T5W1sE4oc1YBuXkVxZzBEYW2a9eyGlI-a6-KIvVK3q4QytKGwGn8zYUSXbACx6HONEhmdydwar6C2HR5_u-jB7OwkvtsxrSVhtg_uXwseHqWZpBN2gXekSOtpoT-rZYZeouUH9NL-lqbnuvUEwjxIEvRDT5xSGSVhCNxngNaynq6p-O8nNjztiFGFDwxUUIX1-mrhfE6WZI8R4kSxqjI3_aWygQd1a-D44i4Qr-q1mKV5EujGzh0xLijIur_z4eEEm9kbZ0Kh6kfPhqMQ"}
```
- Modify the jwt header alg value to symmetric algorithm HS256
- Generate RSA key pair in jwt editor and paste the extracted key
- Copy it as PEM
- Encode it as base64 
- Generate Symm key in jwt editor
- replace k: value with the encoded pem public key