# app/routes/users.py
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models import User, Portfolio
from schemas import UserCreate
from auth import hash_password
from database import get_db
from auth import verify_password, create_access_token

router = APIRouter()

@router.post("/register")
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    hashed_password = hash_password(user.password)
    new_user = User(email=user.email, password=hashed_password)

    new_portfolio = Portfolio(total_value=0.0, user=new_user)
    try:
        db.add(new_user)
        db.add(new_portfolio)
        db.commit()
        return {"message": "User registered successfully"}
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Email already registered.")

@router.post("/login")
def login_user(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    access_token = create_access_token(data={"sub": str(user.id)})
    return {"access_token": access_token, "token_type": "bearer"}