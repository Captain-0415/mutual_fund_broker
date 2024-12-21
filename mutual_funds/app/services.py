import requests
import os
from database import local_session
from dotenv import load_dotenv
from sqlalchemy.orm import Session
from models import MutualFund

load_dotenv()

rapid_url_to_get_latest_nav= os.getenv("RAPID_URL")

headers = {
	"x-rapidapi-key":os.getenv("RAPID_URL_API_KEY"),
	"x-rapidapi-host": "latest-mutual-fund-nav.p.rapidapi.com"
}

#get latest nav from external API
def fetch_latest_nav():
    response = requests.get(rapid_url_to_get_latest_nav, headers=headers, params={"scheme_type": "Open Ended"})
    return response.json()

#update the mutual fund record in the database
def update_mutual_funds():
    db: Session = local_session()
    try:
        data = fetch_latest_nav()

        if not isinstance(data, list):
            raise ValueError("Expected data to be a list of funds, got: {}".format(type(data).__name__))

        for item in data:
            # Debugging: Check the structure of each item

            scheme_code = str(item["Scheme_Code"])
            if not isinstance(item, dict):
                raise ValueError(f"Invalid item structure: {item}")

            # Ensure required keys are present
            required_keys = ["Scheme_Code", "Scheme_Name", "Mutual_Fund_Family", "Net_Asset_Value", "Scheme_Type", "Scheme_Category", "Date"]
            if not all(key in item for key in required_keys):
                raise KeyError(f"Missing keys in item: {item}")

            existing_fund = db.query(MutualFund).filter(MutualFund.scheme_code == scheme_code).first()
            if existing_fund:
                # Update existing record
                existing_fund.nav = item["Net_Asset_Value"]
                existing_fund.date = item["Date"]
            else:
                # Insert new record
                new_fund = MutualFund(
                    scheme_code=scheme_code,
                    scheme_name=item["Scheme_Name"],
                    fund_family=item["Mutual_Fund_Family"],
                    nav=item["Net_Asset_Value"],
                    scheme_type=item["Scheme_Type"],
                    scheme_category=item["Scheme_Category"],
                    date=item["Date"]
                )
                db.add(new_fund)

        db.commit()
        print("Mutual funds updated successfully.")
    except KeyError as e:
        print(f"Error updating mutual funds: Missing key - {e}")
    except ValueError as e:
        print(f"Error updating mutual funds: {e}")
    except Exception as e:
        print(f"Error updating mutual funds: {e}")
    finally:
        db.close()