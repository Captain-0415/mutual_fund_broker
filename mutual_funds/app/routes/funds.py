# app/routes/funds.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import MutualFund
from auth import get_loggedin_user

router = APIRouter()

@router.get("/")
def get_funds(fund_family: str, db: Session = Depends(get_db), current_user=Depends(get_loggedin_user)):
    funds = db.query(MutualFund).filter(MutualFund.fund_family == fund_family).all()
    return {"funds": funds}