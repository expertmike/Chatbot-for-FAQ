import nltk
from nltk.chat.util import Chat, reflections

# Download the necessary resources
nltk.download('punkt')

# Define pairs of patterns and responses
faq_pairs = [
    (r'Hi|Hello|Hey', ['Hello! How can I help you today?', 'Hi there! What can I do for you?']),
    (r'What is your name?', ['I am a chatbot created to assist with your queries.']),
    (r'How can I contact support?', ['You can contact support via email at support@example.com or call us at 123-456-7890.']),
    (r'What are your operating hours?', ['Our operating hours are Monday to Friday, 9 AM to 6 PM.']),
    (r'What services do you offer?', ['We offer a variety of services including customer support, product information, and more.']),
    (r'Thank you|Thanks', ['You\'re welcome! If you have any more questions, feel free to ask.']),
    (r'(.*)', ['I\'m sorry, I didn\'t understand that. Can you please rephrase your question?'])
]

# Create a chatbot instance
faq_chatbot = Chat(faq_pairs, reflections)

def chat_with_bot():
    print("Hello! I'm your FAQ chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Chatbot: Goodbye!")
            break
        response = faq_chatbot.respond(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chat_with_bot()
