from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import User
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
EXPIRY_TIME_MINUTES = 30

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

def verify_password(plain_password, hashed_password)->bool:
    return password_context.verify(plain_password, hashed_password)

def hash_password(password) ->str:
    return password_context.hash(password)

def create_access_token(data: dict):
    to_encode = data.copy()
    expiry = datetime.now() + timedelta(minutes=EXPIRY_TIME_MINUTES)
    to_encode.update({"exp": expiry})
    return jwt.encode(to_encode, SECRET_KEY, algorithm="HS256")

#get logged in user on the basis of JWT Token.
def get_loggedin_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=401, detail="Could not validate credentials", headers={"WWW-Authenticate": "Bearer"}
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        user_id = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise credentials_exception
    return user


