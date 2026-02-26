

class User:
    def __init__(self, age, gender, total_income, expenses):
        self.age = age
        self.gender = gender
        self.total_income = total_income
        self.expenses = expenses # dictionary of categories

    def to_dict(self):
        """Flatten the structure for CSV export."""
        flat = {
            "age": self.age,
            "gender": self.gender,
            "total_income": self.total_income,
        }

        # Add each expense category as two columns
        for category, info in self.expenses.items():
            flat[f"{category}_selected"] = info["selected"]
            flat[f"{category}_amount"] = info["amount"]
            
        return flat
