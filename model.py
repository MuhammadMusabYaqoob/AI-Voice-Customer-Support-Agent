# /mnt/data/model.py
import os
import time
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

# Globals
API_KEY = os.getenv("GEMINI_API_KEY")
_model = None  # will hold genai.GenerativeModel instance
_system_instruction = """You are Grokky, a super helpful and hilarious customer support agent.

Respond to every customer query professionally but with maximum humor, witty remarks, puns, and fun vibes.

Keep it concise: 1-2 sentences max."""
_generation_config = {
    "temperature": 0.7,
    "top_p": 0.8,
    "top_k": 40,
    "max_output_tokens": 150,
}

def configure_model(api_key: str = None):
    """
    Configure the genai client and instantiate the model.
    If api_key is None, it will try to read from environment variable GEMINI_API_KEY.
    """
    global API_KEY, _model
    key = api_key or os.getenv("GEMINI_API_KEY")
    if not key:
        raise ValueError("GEMINI_API_KEY not found. Please set the environment variable or call set_api_key(key).")

    # Configure client
    genai.configure(api_key=key)
    API_KEY = key

    # Instantiate the model
    _model = genai.GenerativeModel(
        "gemini-2.0-flash",
        generation_config=_generation_config,
        system_instruction=_system_instruction
    )
    return _model

def set_api_key(key: str):
    """
    Public helper to set API key at runtime (call from your Gradio app).
    This will both configure genai and instantiate the model.
    """
    return configure_model(api_key=key)

def _ensure_model():
    """
    Ensure that the model is configured. If not, try to configure using env var.
    """
    global _model
    if _model is None:
        configure_model()  # may raise if no key available

def generate_concise_response(prompt: str):
    """
    Generate a concise response from Gemini.

    Returns:
        (response_text: str, response_time_seconds: float)
    """
    try:
        _ensure_model()
        # Start a fresh chat for each request so system instruction is applied consistently
        chat = _model.start_chat(history=[])
        start_time = time.time()
        response = chat.send_message(prompt)
        response_time = time.time() - start_time
        return response.text, response_time
    except Exception as e:
        # Return an error message but keep function signature same
        return f"I apologize, but I encountered an error: {str(e)}", 0.0
