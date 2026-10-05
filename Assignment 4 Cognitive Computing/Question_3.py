import pandas as pd

# Create DataFrame
data = [
    {
        "question": "what is the annual fee",
        "answer": "The annual fee is Rs 500.",
        "keywords": ["fee", "cost", "annual"],
        "category": "billing"
    },
    {
        "question": "how to reset password",
        "answer": "Go to Settings > Reset Password.",
        "keywords": ["password", "reset", "login"],
        "category": "account"
    },
    {
        "question": "what are your working hours",
        "answer": "Our working hours are 9 AM to 5 PM.",
        "keywords": ["hours", "timing", "open time"],
        "category": "general"
    },
    {
        "question": "how can i pay the fee",
        "answer": "You can pay via UPI, card, or net banking.",
        "keywords": ["pay", "payment", "fee"],
        "category": "billing"
    }
]

df = pd.DataFrame(data)


# Function to find entries of the same category
def same_category(category_name, df):
    return df[df["category"] == category_name]


# Use the category "billing"
result = same_category("billing", df)

print("Entries belonging to billing category:")
print(result)