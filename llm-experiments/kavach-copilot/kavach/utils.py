# utilities for the project
import os
from dotenv import load_dotenv
import openai
import requests
from IPython.display import Markdown, display

def get_api_key(key_name):
    """
    Get the API key from the environment variable.
    Load environment variables from .env file
    This is necessary for loading the OpenAI API key
    and other configurations.
    The override=True parameter allows overriding existing variables in the environment
    with the values from the .env file.
    This is useful for testing and development purposes.
    In production, it's recommended to set environment variables directly in the system.
    This way, sensitive information like API keys are not exposed in the code.
    Make sure to create a .env file in the same directory as this script
    with the necessary environment variables.
    Example .env file:
    OPENAI_API_KEY=your_openai_api_key  
    """
    load_dotenv(override=True)
    # Get the API key from the environment variable
    api_key = os.getenv(key_name)
    
    # Check if the API key is valid
    # and not empty
    # If the API key is not found or empty or wrong format, 
    # raise an error
    # If the API key is found, return it
    if not api_key:
        raise ValueError(f"API key '{key_name}' not found. Please set the {key_name} environment variable.")
    elif not api_key.startswith("sk-"):
        raise ValueError(f"Invalid API key format for '{key_name}'. Please check your API key.")
    elif api_key.strip() == "":
        raise ValueError(f"API key '{key_name}' is empty. Please set a valid API key.")
    else:
        print(f"API key '{key_name}' is valid and loaded successfully.")
    return api_key

def messages_for_openai(system_prompt, user_prompt):
    """
    Create a list of messages for the OpenAI API.
    This function takes the system prompt and user prompt as input
    and returns a list of messages in the required format for the OpenAI API.
    """
    # Define the system prompt for the LLM
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
    return messages

def get_openai_response(model, messages):
   
   # Call the OpenAI API
    response = openai.chat.completions.create(
        model=model,
        messages=messages,
        max_tokens=1000,
        temperature=0.7,
    )
    # error handling
    # if response.status_code != 200:
    #     raise Exception(f"Error: {response.status_code} - {response.text}")
    
    return response

# Display the response in Markdown format
def display_markdown(content):
    """
    Display content in Markdown format.
    """
    display(Markdown(content))
   