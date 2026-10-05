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


# Select one entry
entry_index = 0

print("Selected question:")
print(df.loc[entry_index, "question"])


# Ask user for a new keyword
new_keyword = input("Enter a new keyword: ")


# Add the new keyword
df.at[entry_index, "keywords"].append(new_keyword)


# Display updated entry
print("\nUpdated entry:")
print(df.loc[entry_index])


# Roll number
roll_number = "1024170095"

# Save DataFrame as CSV
file_name = f"faq_{roll_number}_faq_data.csv"

df.to_csv(file_name, index=False)

print("\nFile saved successfully as:", file_name)