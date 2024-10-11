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
    
    # Education


    "what is algebra": "Algebra is a branch of mathematics that deals with the study of variables and their relationships.",


    "what is geometry": "Geometry is a branch of mathematics that deals with the study of shapes, sizes, and positions of objects.",


    "what is biology": "Biology is the study of living organisms and their interactions with the environment.",


    "what is chemistry": "Chemistry is the study of the composition, properties, and reactions of matter.",


    # History


    "who was albert einstein": "Albert Einstein was a renowned physicist who developed the theory of relativity and is considered one of the most influential scientists of the 20th century.",


    "who was marie curie": "Marie Curie was a physicist and chemist who was the first woman to win a Nobel Prize and is best known for her pioneering work on radioactivity.",


    "who was charles darwin": "Charles Darwin was a biologist who is best known for his theory of evolution through natural selection.",


    "who was leonardo da vinci": "Leonardo da Vinci was a polymath who is widely considered one of the greatest painters, inventors, and scientists of all time.",


    # Entertainment


    "what is a movie": "A movie is a series of moving images that tell a story or convey information.",


    "what is music": "Music is an art form whose medium is sound and silence.",


    "what is a book": "A book is a written or printed work consisting of pages glued or sewn together.",


    "what is a game": "A game is an activity or contest with rules, undertaken for entertainment or recreation.",


    # Travel


    "what is a country": "A country is a geographical area that is recognized as a separate entity in the international community.",


    "what is a city": "A city is a large human settlement that is typically characterized by a high population density and a complex system of infrastructure.",


    "what is a mountain": "A mountain is a natural elevation of the earth's surface that is usually steeper and taller than a hill.",


    "what is a river": "A river is a natural flowing body of water that often connects lakes, wetlands, and oceans.",


    # Food


    "what is a fruit": "A fruit is the sweet and fleshy part of a plant that develops from the ovary of a flower.",


    "what is a vegetable": "A vegetable is any edible part of a plant, such as the leaves, stems, roots, or tubers.",


    "what is a meat": "A meat is the flesh of an animal that is used as food.",


    "what is a dessert": "A dessert is a sweet dish that is typically served after a meal.",

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