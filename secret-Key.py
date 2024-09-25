import os
import secrets

# Generate a new secret key
secret_key = secrets.token_urlsafe(50)

# Print the secret key
print("SECRET_KEY = '{}'" .format(secret_key))
