import pandas as pd

# Enter your roll number
roll_number = "1024170095"       # CHANGE THIS TO YOUR ROLL NUMBER

# Take last two digits
digits = [int(d) for d in roll_number[-2:]]

# Category list
categories = ["billing", "account", "general"]

# Fixed 4 entries
fixed_entries = [
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

# Create 2 personalized entries
personalized_entries = []

for digit in digits:

    category = categories[digit % 3]

    question = f"how do I update my {category} details for roll number {roll_number}"
    answer = f"You can update your {category} details from the settings section."

    keywords = [category, "details", "update"]

    personalized_entries.append({
        "question": question,
        "answer": answer,
        "keywords": keywords,
        "category": category
    })

# Combine fixed and personalized entries
all_entries = fixed_entries + personalized_entries

# Create DataFrame
df = pd.DataFrame(all_entries)

# Print final 6-row DataFrame
print(df)