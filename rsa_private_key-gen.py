from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# Example prime factors of n

p = # your prime factors of n
q = # your prime factors of n
e = 65537

# Calculate the necessary components for the private key
n = p * q
phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)

# Create the private key object
private_key = rsa.RSAPrivateNumbers(
    p=p,
    q=q,
    d=d,
    dmp1=d % (p - 1),
    dmq1=d % (q - 1),
    iqmp=pow(q, -1, p),
    public_numbers=rsa.RSAPublicNumbers(e=e, n=n)
).private_key(default_backend())

# Serialize private key to PEM format
pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
)

# Write pem to a file
with open("private_key.pem", "wb") as f:
    f.write(pem)

print("RSA private key has been saved to 'private_key.pem'.")
