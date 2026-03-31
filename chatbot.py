#Rule-Based Chatbot
print("🍔 Restaurant Chatbot (type 'bye' to exit)\n")

while True:
    user_input = input("You: ").lower()

    if "hi" in user_input:
        print("Bot: Welcome to Food Corner!")

    elif "menu" in user_input:
        print("Bot: We have pizza, burger, pasta, and drinks.")

    elif "price" in user_input:
        print("Bot: Prices start from ₹100.")

    elif "order" in user_input:
        print("Bot: Please visit the counter to place your order.")

    elif "timing" in user_input:
        print("Bot: We are open from 10 AM to 10 PM.")

    elif "location" in user_input:
        print("Bot: We are near City Mall.")

    elif user_input == "bye":
        print("Bot: Thank you! Visit again.")
        break

    else:
        print("Bot: Sorry, I didn't understand.")