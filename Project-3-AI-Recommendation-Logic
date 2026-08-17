database = [
    {"title": "Python for Beginners", "tags": ["python", "programming", "easy"]},
    {"title": "Advanced Machine Learning", "tags": ["ai", "python", "hard", "data"]},
    {"title": "Web Development with HTML & CSS", "tags": ["web", "css", "easy", "frontend"]},
    {"title": "Data Science Fundamentals", "tags": ["ai", "data", "medium", "python"]},
    {"title": "JavaScript Mastery", "tags": ["web", "javascript", "medium", "frontend"]},
    {"title": "Rule-Based Chatbots", "tags": ["ai", "python", "medium", "logic"]}
]

def get_recommendation(user_interests):
    user_tags = [tag.lower().strip() for tag in user_interests.split(",")]
    scored_items = []

    for item in database:
        score = 0
        for user_tag in user_tags:
            if user_tag in item["tags"]:
                score += 1

        if score > 0:
            scored_items.append({"title": item["title"], "score": score})

    scored_items.sort(key=lambda x: x["score"], reverse=True) 
    return scored_items
   
def main():
    print("=== DecodeLabs Project 3: AI Recommendation Logic ===")
    print("Enter your interests separated by commas (e.g., python, ai, web):")                    

    user_interests = input("what are you interested in today?")
    results = get_recommendation(user_interests)
    print("\n--- Recommended Results for You ---")

    if not results:
        print("sorry, we couldn't find an exact match. Try using different keywords")

    else:
        for idx, item in enumerate (results, 1):
            print(f"{idx}. {item['title']} (Match Score: {item['score']})")

if __name__== "__main__":
    main()
