# AI Text Completion App (Cohere API)

This is a terminal-based Python application that uses the Cohere API to generate text completions based on user input. You can customize the `max_tokens` and `temperature` values for each prompt.

## Setup Instructions

1. Clone the Repository

2. Create and Activate a Virtual Environment
python3 -m venv .venv
source .venv/bin/activate  # Mac/Linux
.venv\Scripts\activate     # Windows

3. Install Dependencies
pip install cohere python-dotenv

4. Add Your API Key
Create a .env file in the root of the project:
COHERE_API_KEY=your_cohere_api_key_here
Make sure this file is included in your .gitignore.

5.How to Run
python text_completion_app.py
You’ll be prompted to enter:

A text prompt (e.g., "Explain gravity")

A max token count (between 10 and 512)

A temperature (between 0.0 and 1.0)

The app will return a generated completion using Cohere’s command-nightly model.
