# Signature is validated
## Symmetric alg is used for the signing
trying to crack the password used for HMAC using hashcat
`hashcat -a 0 -m 16500 <JWT> <Wordlist>`
secret1 is the key => modify the JWT's payload, sign it with the new forged signature