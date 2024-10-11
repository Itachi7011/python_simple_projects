# Define a dictionary to store the responses

responses = {

    "hello": "Hello! How can I assist you today?",

    "hi": "Hi! What's on your mind?",

    "hey": "Hey! How's it going?",

    "hi there": "Hi there! How can I help you?",

    "hello there": "Hello there! What brings you here?",

    # Goodbyes

    "goodbye": "Goodbye! It was nice chatting with you.",

    "bye": "Bye! See you later!",

    "see you later": "See you later! Have a great day!",

    "farewell": "Farewell! It was nice talking to you.",

    # Thanks and appreciation

    "thanks": "You're welcome!",

    "thank you": "You're welcome!",

    "appreciate it": "You're welcome! I'm happy to help.",

    "thank you so much": "You're welcome! It was my pleasure.",

    # Emotions and sentiments

    "i'm happy": "That's great to hear! What's making you happy today?",

    "i'm sad": "Sorry to hear that. Would you like to talk about what's bothering you?",

    "i'm angry": "I understand. Would you like to talk about what's making you angry?",

    "i'm frustrated": "I'm here to listen. What's frustrating you?",

    # Definitions

    "what is ai": "AI stands for Artificial Intelligence, which refers to the development of computer systems that can perform tasks that typically require human intelligence.",

    "what is machine learning": "Machine learning is a subset of AI that involves training algorithms to learn from data and make predictions or decisions without being explicitly programmed.",

    "what is deep learning": "Deep learning is a subset of machine learning that involves the use of neural networks to analyze data and make predictions or decisions.",

    # Topics to discuss

    "what's up": "Not much! How about we talk about the latest news, sports, or entertainment?",

    "what's new": "Not much! How about we discuss the latest advancements in AI, space exploration, or technology?",

    "what's interesting": "I've got a few topics in mind. How about we talk about the latest scientific discoveries, historical events, or cultural trends?",
    
    

    # Help and quit

    "help": "I can understand the following commands: hello, hi, goodbye, bye, thanks, thank you. Type 'quit' to exit the chatbot.",

    "quit": "Goodbye! It was nice chatting with you.",

    # Default response

    "default": "I didn't understand that. Can you please rephrase?"

}


# Define a list to store the conversation history

conversation_history = []


# Define a function to get the user's input and respond accordingly

def chatbot():

    print("Welcome to the chatbot! Type 'help' for available commands or 'quit' to exit.")

    while True:

        user_input = input("You: ").lower()

        conversation_history.append(user_input)

        if user_input == "quit":

            print("Bot: Goodbye! It was nice chatting with you.")

            break

        elif user_input in responses:

            print("Bot:", responses[user_input])

        else:

            # Check for multiple-word inputs

            words = user_input.split()

            for word in words:

                if word in responses:

                    print("Bot:", responses[word])

                    break

            else:

                print("Bot:", responses["default"])


    # Print the conversation history

    print("\nConversation History:")

    for i, message in enumerate(conversation_history, start=1):

        print(f"{i}. You: {message}")


# Run the chatbot

chatbot()