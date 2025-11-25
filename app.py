import gradio as gr
import time
import os
import google.generativeai as genai

from sst import transcribe_audio
from model import generate_concise_response
from tts import text_to_speech

# -----------------------------
# SAVE API KEY
# -----------------------------
def save_api_key(user_key):
    if not user_key or user_key.strip() == "":
        return "❌ API key cannot be empty.", gr.update(visible=False), gr.update(visible=False), gr.update(selected=0)
    
    os.environ["GEMINI_API_KEY"] = user_key.strip()
    
    try:
        genai.configure(api_key=user_key.strip())
        return "✅ API key saved successfully! Chat and History tabs are now unlocked.", gr.update(visible=True), gr.update(visible=True), gr.update(selected=1)
    except Exception as e:
        return f"❌ Invalid API Key: {str(e)}", gr.update(visible=False), gr.update(visible=False), gr.update(selected=0)

# -----------------------------
# PROCESS QUERY
# -----------------------------
def process_query(audio, user_text, history):
    history = history or []
    
    text = user_text.strip() if user_text and user_text.strip() else None
    audio_used = False

    if not text:
        if not audio:
            return "", None, "Please type a message or record audio.", history, gr.update(value=None), history
        
        transcribed = transcribe_audio(audio)
        if not transcribed:
            return "", None, "No speech detected. Please try again.", history, gr.update(value=None), history
        
        text = transcribed
        audio_used = True
        print(f"👤 YOU SAID: '{text}'")
    else:
        print(f"👤 YOU TYPED: '{text}'")
    
    print("🤖 GENERATING RESPONSE...")
    response_text, generate_time = generate_concise_response(text)
    print(f"🤖 AGENT: {response_text}")

    bot_md = f"**🤖 Assistant:**\n\n{response_text}"
    
    tts_file = f"response_{int(time.time() * 1000)}.mp3"
    tts_success = text_to_speech(response_text, tts_file)
    
    user_content = [text, gr.Audio(value=audio)] if audio_used else text
    
    if tts_success:
        assistant_content = [response_text, gr.Audio(value=tts_file)]
        new_history = history + [
            {"role": "user", "content": user_content},
            {"role": "assistant", "content": assistant_content}
        ]
        return bot_md, tts_file, "", new_history, gr.update(value=None), new_history
    
    else:
        assistant_content = f"{response_text} (Audio generation failed)"
        new_history = history + [
            {"role": "user", "content": user_content},
            {"role": "assistant", "content": assistant_content}
        ]
        return bot_md, None, "", new_history, gr.update(value=None), new_history

# -----------------------------
# CLEAR CHAT
# -----------------------------
def clear_chat():
    return "", None, "", [], gr.update(value=None), []

# -----------------------------
# UI WITH TABS
# -----------------------------
with gr.Blocks(title="AI Voice Agent") as demo:
    
    chat_history = gr.State([])
    
    gr.Markdown("""
# 🎤 AI Voice Customer Support Agent
Powered by Whisper, Gemini 2.0 Flash, gTTS
    """)
    
    gr.Markdown("**Start by entering your API key in the first tab.**")
    
    with gr.Tabs() as tabs:
        
        # Tab 1: API Key
        with gr.TabItem("🔑 1. API Key") as api_tab:
            gr.Markdown("""
## Enter your Gemini API Key to unlock other tabs
            """)
            
            api_input = gr.Textbox(
                label="Gemini API Key",
                placeholder="AIza... paste your key here"
            )
            
            save_key_btn = gr.Button("💾 Save API Key", variant="primary")
            api_status = gr.Markdown("")
            
            gr.Markdown("### Other Actions")
            clear_btn_api = gr.Button("🗑️ Clear Chat History")
        
        # Tab 2: Chat (initially hidden)
        with gr.TabItem("💬 2. Ask Query", visible=False) as chat_tab:
            gr.Markdown("### Chat Interface")
            
            # Input row
            with gr.Row():
                record_btn = gr.Microphone(
                    type="filepath",
                    label="🎤 Record"
                )
                
                transcribed_text = gr.Textbox(
                    placeholder="Type your message or use voice input...",
                    show_label=False,
                    lines=3
                )
                
                submit_btn = gr.Button("Send ➤", variant="primary")
            
            gr.Markdown("---")
            
            # Response audio
            response_audio = gr.Audio(
                label="🤖 Model Response",
                autoplay=True
            )
            
            gr.Markdown("---")
            
            gr.Markdown("### 🤖 Assistant Response")
            response_text_md = gr.Markdown("")
            
            gr.Markdown("---")
            clear_btn_chat = gr.Button("🗑️ Clear Chat")
        
        # Tab 3: History (initially hidden)
        with gr.TabItem("📜 3. History", visible=False) as history_tab:
            history_chatbot = gr.Chatbot(
                label="💬 Full Conversation History",
                height=500,
                avatar_images=("https://api.dicebear.com/7.x/avataaars-neutral/svg?seed=user", "https://api.dicebear.com/7.x/bottts/svg?seed=bot")
            )
    
    # -----------------------------
    # EVENTS
    # -----------------------------
    save_key_btn.click(
        save_api_key,
        inputs=[api_input],
        outputs=[api_status, chat_tab, history_tab, tabs]
    )
    
    submit_btn.click(
        process_query,
        inputs=[record_btn, transcribed_text, chat_history],
        outputs=[response_text_md, response_audio, transcribed_text, chat_history, record_btn, history_chatbot]
    )
    
    clear_btn_chat.click(
        clear_chat,
        outputs=[response_text_md, response_audio, transcribed_text, chat_history, record_btn, history_chatbot]
    )
    
    clear_btn_api.click(
        clear_chat,
        outputs=[response_text_md, response_audio, transcribed_text, chat_history, record_btn, history_chatbot]
    )

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
