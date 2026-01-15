import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Initialize Gemini client
client = genai.Client(api_key=api_key)

# Send a prompt to Gemini
response = client.models.generate_content(
    model="gemini-3-flash-preview", 
    contents="In one or two sentences, how does an AI Engineer differ from a Software Engineer?"
)

print(response.text)
