# app/routes/portfolio.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import Portfolio, Investment, MutualFund
from database import get_db
from schemas import InvestmentCreate
from auth import get_loggedin_user

router = APIRouter()

@router.post("/invest")
def invest_in_fund(
    investment: InvestmentCreate, 
    db: Session = Depends(get_db), 
    current_user=Depends(get_loggedin_user)
):
    # Fetch mutual fund and user's portfolio
    mutual_fund = db.query(MutualFund).filter(MutualFund.id == investment.mutual_fund_id).first()
    portfolio = db.query(Portfolio).filter(Portfolio.user_id == current_user.id).first()

    if not portfolio:
        return {"error": "Portfolio not found"}

    # Create a new investment record
    new_investment = Investment(
        portfolio_id=portfolio.id,
        mutual_fund_id=mutual_fund.id,
        mutual_fund_name=mutual_fund.scheme_name,
        units=investment.units,
        purchase_price=investment.purchase_price
    )
    db.add(new_investment)

    # Update portfolio's total value
    portfolio.total_value += investment.units * mutual_fund.nav

    # Commit changes to the database
    db.commit()
    db.refresh(new_investment)

    return {
        "message": "Investment added successfully",
        "investment": {
            "mutual_fund_id": new_investment.mutual_fund_id,
            "mutual_fund_name": new_investment.mutual_fund_name,
            "units": new_investment.units,
            "purchase_price": new_investment.purchase_price
        }
    }
@router.get("/fetch")
def calculate_portfolio(db: Session = Depends(get_db), current_user=Depends(get_loggedin_user)):
    portfolio = db.query(Portfolio).filter(Portfolio.user_id == current_user.id).first()
    if not portfolio:
        return {"error": "Portfolio not found"}

    # Fetch investments dynamically from the database
    investments = db.query(Investment).filter(Investment.portfolio_id == portfolio.id).all()

    # Prepare investment details for the response
    investment_details = [
        {
            "mutual_fund_id": investment.mutual_fund_id,
            "mutual_fund_name": investment.mutual_fund_name,
            "units": investment.units,
            "purchase_price": investment.purchase_price
        }
        for investment in investments
    ]

    return {
        "total_value": portfolio.total_value,
        "investments": investment_details
    }