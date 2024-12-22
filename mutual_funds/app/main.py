# app/main.py
from fastapi import FastAPI, Request
from database import engine, Base
from routes import users, funds, portfolio
from services import update_mutual_funds
from apscheduler.schedulers.background import BackgroundScheduler
from starlette.responses import RedirectResponse
import logging

app = FastAPI()

# Initialize database
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(users.router, prefix="/users")
app.include_router(funds.router, prefix="/funds")
app.include_router(portfolio.router, prefix="/portfolio")

# Scheduler to get latest nav data hourly
scheduler = BackgroundScheduler()
def app_lifespan(app):
    # Startup actions
    update_mutual_funds()  # Run initial update
    print("Initial mutual funds update completed.")
    scheduler.add_job(update_mutual_funds, "interval", hours=1)
    scheduler.start()
    logging.info("Scheduler started.")

    # Shutdown actions
    yield
    scheduler.shutdown()
    logging.info("Scheduler stopped.")

app = FastAPI(lifespan=app_lifespan)

app.include_router(users.router, prefix="/users")
app.include_router(funds.router, prefix="/funds")
app.include_router(portfolio.router, prefix="/portfolio")

custom_docs_url = "https://mutual-funds-api.apidog.io/"
@app.middleware("http")
async def apidog_docs_redirect(request: Request, call_next):
    if request.url.path == "/docs":
        return RedirectResponse(url=custom_docs_url, status_code=307)
    return await call_next(request)