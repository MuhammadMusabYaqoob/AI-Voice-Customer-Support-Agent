from gtts import gTTS
import os

def text_to_speech(text, filename):
    """Convert text to speech and save to file"""
    try:
        tts = gTTS(text=text, lang='en', slow=False)
        tts.save(filename)
        return True
    except Exception as e:
        print(f"TTS error: {e}")
        return False