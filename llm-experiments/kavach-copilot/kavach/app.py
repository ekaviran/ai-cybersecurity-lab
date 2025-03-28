# @author: Gautam Muralidharan
# @date: 2023-10-01
# @description: This file contains the main application logic for the Kavach Copilot.
# @license: MIT

import gradio as gr
import kavach.analyzer as analyze_code

def run_analysis(code_input):
    return analyze_code(code_input)

iface = gr.Interface(
    fn=run_analysis,
    inputs=gr.Code(language="python", label="Paste your Python code"),
    outputs=gr.Textbox(label="Security Analysis"),
    title="🛡️ Kavach-Copilot",
    description="Paste your code below and Kavach will analyze it for security vulnerabilities."
)

if __name__ == "__main__":
    iface.launch()
