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


# Function to score the query
def score_query(query, df):

    query = query.lower()

    results = []

    for index, row in df.iterrows():

        score = 0

        for keyword in row["keywords"]:

            if keyword.lower() in query:
                score += 1

        if score > 0:
            results.append({
                "question": row["question"],
                "answer": row["answer"],
                "category": row["category"],
                "score": score
            })

    # Convert results into DataFrame
    result_df = pd.DataFrame(results)

    # Sort by highest score
    if not result_df.empty:
        result_df = result_df.sort_values(
            by="score",
            ascending=False
        )

    return result_df


# Test query
query = "How can I pay my annual fee?"

result = score_query(query, df)

print("Query:", query)

print("\nMatching entries:")

print(result)