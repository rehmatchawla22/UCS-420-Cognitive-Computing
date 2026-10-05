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


# Modified scoring function
def score_query_with_ties(query, df):

    query = query.lower()

    results = []

    # Calculate score for every entry
    for index, row in df.iterrows():

        score = 0

        for keyword in row["keywords"]:

            if keyword.lower() in query:
                score += 1

        results.append({
            "question": row["question"],
            "answer": row["answer"],
            "category": row["category"],
            "score": score
        })

    # Convert results to DataFrame
    result = pd.DataFrame(results)

    # Find highest score
    highest_score = result["score"].max()

    # Return ALL entries having highest score
    top_results = result[result["score"] == highest_score]

    return top_results


# Test 1: Query matching both "fee" entries
query1 = "fee"

result1 = score_query_with_ties(query1, df)

print("Query 1:", query1)
print("\nTop matching entries:")
print(result1)


# Test 2: Query that does not match any keyword
query2 = "computerxyz"

result2 = score_query_with_ties(query2, df)

print("\n\nQuery 2:", query2)
print("\nTop matching entries:")
print(result2)