import re

# Sample messages
with open(r"_chat.txt", 'r', encoding="utf-8") as fp:
    text = fp.readlines()

# Define categories and corresponding keywords
categories = {
    "Coding/Doubt Clearance": ["coding", "doubt", "question", "help", "python", "Google Meet"],
    "Photography": ["photography", "photo", "picture", "camera"],
    "Conducting Contests": ["contest", "competition", "aptitude test", "quiz"],
    "Events": ["hackathon", "event", "meeting", "gathering"],
    "Facts of the Day": ["important to share","Today's discussion is about","fact", "interesting fact", "did you know"],
}

# Function to categorize a message
def categorize_message(message):
    message = message.lower()  # Convert to lowercase for case-insensitivity

    for category, keywords in categories.items():
        for keyword in keywords:
            if re.search(r'\b' + re.escape(keyword) + r'\b', message):
                return category

    return "Personal Chat"  # Default category

# Categorize each message
message_categories = {}

for message in text:
    category = categorize_message(message)
    if category not in message_categories:
        message_categories[category] = [message]
    else:
        message_categories[category].append(message)

# Display categorized messages
for category, messages in message_categories.items():
    print(f'Category: "{category}"')
    for message in messages:
        print(f'- "{message}"')

# Summary
for category, messages in message_categories.items():
    print(f'Total messages in category "{category}": {len(messages)}')
