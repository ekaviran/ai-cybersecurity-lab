# Ver 1.0
# @author: Gautam Muralidharan
# @date: 2023-10-01
# @description: This file contains the Analyzer class which is responsible for analyzing the code and providing suggestions.
# @license: MIT

# import os
# import requests
import gradio as gr
# from dotenv import load_dotenv
#from bs4 import BeautifulSoup
# from IPython.display import Markdown, display
from openai import OpenAI
from utils import get_api_key, messages_for_openai, \
    message_gpt, display_markdown

OPENAI_MODEL = "gpt-4o-mini"

# Load environment variables from .env file

api_key = get_api_key("OPENAI_API_KEY")

# Initialize OpenAI API client
openai = OpenAI()

# message = "Hello, GPT! This is a test message."
# response = openai.chat.completions.create(
#     model=OPENAI_MODEL,
#     messages=[{"role": "user", "content": message}],
#     max_tokens=100,
#     temperature=0.7,
# )
# print(response.choices[0].message.content)

# blob of code to test 
# SAMPLE_CODE = """
# def add(a, b):
#     return a + b
# def subtract(a, b): 
#     return a - b
# def multiply(a, b):     
#     return a * b
# def divide(a, b):                   
#     if b == 0:
#         raise ValueError("Cannot divide by zero")
#     return a / b    "
#     """

# Define the system prompt for the LLM
LANGUAGE= "python"
system_prompt = f"""
You are a highly skilled secure code analyzer. You will be provided with a block of {LANGUAGE} code.

Your task is to:
1. Identify potential security vulnerabilities in the code.
2. Provide clear, actionable suggestions to improve the security of the code.
3. Summarize the overall security posture of the code (e.g., low/medium/high risk).
4. Explain any relevant secure coding best practices or OWASP Top 10 principles that apply.

Be concise, use bullet points, and avoid unnecessary filler text.
"""

# user_prompt = f"""
# Analyze the following Python code for security vulnerabilities:
# {SAMPLE_CODE}
# """

print("System Prompt:\n", system_prompt)
# print("User Prompt:\n", user_prompt)



# Call the OpenAI API
# response = message_gpt(OPENAI_MODEL, messages)
# Print the response
# print("Response from OpenAI API:\n", response)

# display_markdown(response)

view = gr.Interface(
    fn=message_gpt,
    inputs=[
        # gr.inputs.Textbox(label="System Prompt", default=system_prompt),
        gr.Textbox(label="Code Input", lines=10, placeholder="Paste your code here..."),
    ],
    outputs=gr.Textbox(label="Response", lines=20, placeholder="Response from OpenAI API..."),
    title="Secure Code Analyzer",
    description="Analyze code for security vulnerabilities and get suggestions.",
    theme="default"
)
view.launch()

# messages = messages_for_openai(system_prompt, user_prompt)

# gr.Interface(fn=message_gpt,inputs="text", outputs="text").launch()