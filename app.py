# Flask app with MongoDB Storage + Validation + Success page

from flask import Flask, render_template, request
from pymongo import MongoClient
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()     # loads .env automatically

# --- MongoDB Connection (Use Environment Variable in Production---
mongo_uri = os.getenv("MONGO_URI")
if not mongo_uri:
    raise ValueError("MONGO_URI.environment variable is missing!")

print("MONGO_URI:", mongo_uri)

client = MongoClient(mongo_uri)
db = client["flask_health_care_app"]
users_collection = db["users"]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        # basic user details
        try:
            # --- Basic user details ---
            age = int(request.form.get("age"))
            gender = request.form.get("gender")
            income = float(request.form.get("income"))
        except (ValueError, TypeError):
            return render_template(
                "form.html",
                error="Please enter valid numeric values for Age and Income."
            )

        # --- Expense Categories ---
        expense_categories = {
            "utilities": ("utilities_checkbox", "utilities_amount"),
            "entertainment": ("entertainment_checkbox", "entertainment_amount"),
            "school_fees": ("school_checkbox", "school_amount"),
            "shopping": ("shopping_checkbox", "shopping_amount"),
            "healthcare": ("healthcare_checkbox", "healthcare_amount"),
        }

        expenses = {}

        for category, (checkbox, amount_field) in expense_categories.items():
            selected = request.form.get(checkbox) == "on"
            amount_value = request.form.get(amount_field)

            # Validation: Prevent entering amount without checking checkbox
            
            if amount_value and not selected:
                return render_template(
                    "form.html",
                    error=f"You entered an amount for {category.replace('_', '').title()} without selecting the checkbox."
                )

            try:
                amount = float(amount_value) if amount_value else 0
            except ValueError:
                return render_template(
                    "form.html",
                    error=f"Invalid amount entered for {category.replace('_','').title()}."
                )

            expenses[category] = {
                "selected": selected,
                "amount": amount
            }

        # --- Build MongoDB Document ---
        user_data = {
            "age": age,
            "gender": gender,
            "total_income": income,
            "expenses": expenses
        }

        users_collection.insert_one(user_data)

        return render_template("success.html", user=user_data)

    return render_template("form.html")
     

# ------Run the Flask App -------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

   
