# Signature is not validated
Trying to delete the signature part of the jwt does not invoke any unauthorized errors so signature is not checked in the backend
## By decoding the payload sub key is responsible for distinguishing admins from users
Replacing wiener with administrator and encoding the modified token then trying to access /admin
## Successful!