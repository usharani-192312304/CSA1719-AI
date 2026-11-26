
import nltk
import random
from nltk.chat.util import Chat, reflections

# Define chatbot patterns and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I help you?", "Hi! Nice to meet you."]
    ],
    [
        r"what is your name?",
        ["I am a simple Python chatbot."]
    ],
    [
        r"how are you?",
        ["I am fine! How are you?"]
    ],
    [
        r"what is python?",
        ["Python is a popular programming language."]
    ],
    [
        r"bye|goodbye",
        ["Goodbye! Have a nice day."]
    ],
    [
        r"(.*)",
        ["Sorry, I don't understand."]
    ]
]

# Create chatbot
chatbot = Chat(pairs, reflections)

# Start conversation
print("Chatbot: Hello! Type 'bye' to exit.")
chatbot.converse()
