# app/schemas.py
from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    email: str
    password: str

class MutualFundResponse(BaseModel):
    scheme_code: str
    scheme_name: str
    nav: float
    fund_family: str
    scheme_type: str
    scheme_category: str
    date: str

class InvestmentCreate(BaseModel):
    mutual_fund_id: int
    units: float
    purchase_price: float