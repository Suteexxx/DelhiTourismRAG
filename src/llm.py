import os
from google import genai
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# The new client automatically searches for an environment variable 
# named GEMINI_API_KEY, so we don't even need to pass it explicitly.
client = genai.Client()

def generate_answer(prompt: str) -> str:
    """Generates a text response using the gemini-2.5-flash model."""
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )
    return response.text

# Quick test execution block
if __name__ == "__main__":
    test_prompt = "Give me a 1-sentence interesting fact about Delhi."
    print(f"Prompt: {test_prompt}\n")
    try:
        answer = generate_answer(test_prompt)
        print(f"Response:\n{answer}")
    except Exception as e:
        print(f"Error generating content: {e}")