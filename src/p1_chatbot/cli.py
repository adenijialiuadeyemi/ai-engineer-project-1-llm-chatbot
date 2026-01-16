"""
Chatbot CLI using Google Gemini
--------------------------------
Features:
- Runs a continuous loop until the user types "exit", "quit", or "/quit"
- Accepts user input from the command line
- Sends input to Gemini with conversation context
- Prints the AI's response
- Ignores empty input (just reprompts)
"""

import os
from dotenv import load_dotenv
from google import genai

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")


def main():
    """
    Main entrypoint for the chatbot CLI.
    Initializes the Gemini client and runs the chat loop.
    """
    # Initialize Gemini client with API key
    client = genai.Client(api_key=api_key)

    # Create a chat session once (so history is preserved across turns)
    chat = client.chats.create(model="gemini-2.5-flash")

    while True:
        # Prompt user for input
        user_input = input("You: ").strip()

        # Exit conditions (case-insensitive)
        if user_input.lower() in ["quit", "exit", "/quit"]:
            print("Exiting chatbot. Goodbye!")
            break

        # Ignore empty input (reprompt without calling API)
        if not user_input:
            continue

        # Send user input to Gemini with conversation history
        response = chat.send_message(user_input)

        # Print assistant response
        print("AI:", response.text)


# Run main() if executed directly
if __name__ == "__main__":
    main()
