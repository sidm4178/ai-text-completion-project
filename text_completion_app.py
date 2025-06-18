import os
import cohere
from dotenv import load_dotenv

# Load API key
load_dotenv()
api_key = os.getenv("COHERE_API_KEY")
co = cohere.Client(api_key)

# Helper: get valid max_tokens
def get_valid_max_tokens():
    while True:
        try:
            val = int(input("Enter max tokens (10–512): "))
            if 10 <= val <= 512:
                return val
            print("Invalid input. Must be between 10 and 512.")
        except ValueError:
            print("Please enter a valid integer.")

# Helper: get valid temperature
def get_valid_temperature():
    while True:
        try:
            val = float(input("Enter temperature (0.0–1.0): "))
            if 0.0 <= val <= 1.0:
                return val
            print("Invalid input. Must be between 0.0 and 1.0.")
        except ValueError:
            print("Please enter a valid float.")

print("\nWelcome to the AI text completer!\n")

# Prompt loop
while True:
    prompt = input("\nEnter a prompt for the AI to use (or 'Exit' to exit): ").strip()

    if not prompt:
        print("Your input cannot be empty! Must be a prompt or 'Exit'.")
        continue
    if prompt.lower() == "exit":
        print("Thank you for using the AI text completer!")
        break

    max_tokens = get_valid_max_tokens()
    temperature = get_valid_temperature()

    try:
        print("\nSending request to Cohere...\n")
        response = co.chat(
            message=prompt,
            model="command-nightly",
            temperature=temperature,
            max_tokens=max_tokens
        )
        print("Generated response:\n", response.text.strip())
    except Exception as e:
        print("Error communicating with Cohere API:", e)
