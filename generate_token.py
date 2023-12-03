import jwt
from datetime import datetime, timedelta

# Define your secret key and algorithm
SECRET_KEY = "your_secret_key"  # Replace with your actual secret key
ALGORITHM = "HS256"  # The algorithm used to create the JWT

def create_test_token():
    payload = {
        "sub": "test_user",  # Subject of the token (change as needed)
        "exp": datetime.utcnow() + timedelta(hours=1)  # Token expires in 1 hour
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

if __name__ == "__main__":
    token = create_test_token()
    print("Generated JWT Token:")
    print(token)
