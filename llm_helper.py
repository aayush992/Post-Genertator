from dotenv import load_dotenv  # Corrected spelling of `dotenv`
from langchain_groq import ChatGroq
import os

# Load the environment variables from the .env file
load_dotenv()  # Fixed the typo `load dotnev()`

# Initialize ChatGroq with the API key from the environment variables
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),  # Fixed `os.getnev` to `os.getenv`
    model_name="llama-3.2-90b-text-preview"  # Corrected spelling of "llama" and "preview"
)

# Example: Check if the script runs without errors
if __name__ == "__main__":
    response = llm.invoke("Two most important ingrident in samosa are ")
    print(response.content)
