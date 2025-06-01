import random

# Define patterns and responses
responses = {
    "hi": ["Hello!", "Hi there!", "Hey, how's it going?"],
    "hello": ["Hey!", "Hi!", "Nice to see you!"],
    "how are you": ["I'm good, how about you?", "Doing great!", "All systems are running smoothly."],
    "what's your name": ["I'm ChatBot!", "Call me ChatBot.", "Your friendly chatbot here!"],
    "bye": ["Goodbye!", "See you later!", "Bye, take care!"],
    "default": ["Sorry, I didn't understand that.", "Could you rephrase that?", "Hmm, that's new to me."]
}

# Normalize user input and match loosely
def match_input(user_input):
    user_input = user_input.lower().strip()

    for key in responses:
        if key in user_input:
            return key

    return "default"

def get_response(user_input):
    matched_key = match_input(user_input)
    return random.choice(responses[matched_key])

# Main chat loop
def chat():
    print("ChatBot 🤖: Hello! Type 'bye' anytime to exit.\n")

    while True:
        user_input = input("You: ")
        if "bye" in user_input.lower():
            print("ChatBot 🤖: Goodbye! 👋")
            break

        print(f"ChatBot 🤖: {get_response(user_input)}")

# Run the chatbot
if __name__ == "__main__":
    chat()
