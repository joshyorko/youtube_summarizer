import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timezone

# Define your secret key and algorithm
SECRET_KEY = "your_secret_key"  # Replace with your actual secret key
ALGORITHM = "HS256"  # The algorithm you used to create the JWT

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def validate_token(token: str) -> bool:
    try:
        # Decode the token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        # Check if the token has expired
        exp = payload.get("exp")
        if exp and datetime.fromtimestamp(exp, timezone.utc) < datetime.now(timezone.utc):
            return False

        # Here, you can add more checks, like user role, token issuer, etc.

        return True
    except jwt.PyJWTError:
        return False

def get_current_user(token: str = Depends(oauth2_scheme)):
    if not validate_token(token):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials"
        )
    # In a real scenario, you might query your user database here
    # For simplicity, returning the token itself
    return token
