import os


# Connect to the assistant
    # Set up OpenAI key
    # Use assistant ID to retrieve the assistant

# Check for OpenAI API key
assert os.environ.get('OPENAI_API_KEY'), "OPENAI_API_KEY not found in .env file."
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

# Function for prompting the assistant
    # Take the thread, word and translation as params
    # Format them into a message and run it
    # Return the result

# Iterate through the CSV and generate an association for each one
    # Create the thread
    # First test with the first few rows
