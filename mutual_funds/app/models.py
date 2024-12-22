from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSON
from database import Base

class User(Base):
    __tablename__="users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    portfolio = relationship("Portfolio", back_populates="user", uselist=False)

class MutualFund(Base):
    __tablename__="mutual_fund"
    id = Column(Integer, primary_key=True, index=True)
    scheme_code = Column(String, unique=True, index=True)
    scheme_name = Column(String)
    fund_family = Column(String, index=True)
    scheme_name = Column(String)
    nav = Column(Float)
    scheme_type = Column(String)
    scheme_category = Column(String)
    date = Column(DateTime)

class Portfolio(Base):
    __tablename__="portfolio"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    total_value = Column(Float)
    investments_summary = Column(JSON, default={})
    user = relationship("User", back_populates="portfolio")

class Investment(Base):
    __tablename__="investment"
    id = Column(Integer, primary_key=True, index=True)
    portfolio_id = Column(Integer, ForeignKey("portfolio.id"))
    mutual_fund_id = Column(Integer, ForeignKey("mutual_fund.id"))
    mutual_fund_name = Column(String)
    units = Column(Float)
    purchase_price = Column(Float)


