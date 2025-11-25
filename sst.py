import whisper
import os

whisper_model = whisper.load_model("base")

def transcribe_audio(audio_path):
    """Transcribe audio file using Whisper"""
    if not audio_path or not os.path.exists(audio_path):
        return ""
    try:
        result = whisper_model.transcribe(audio_path, language="en", fp16=False, temperature=0, beam_size=1)
        return result["text"].strip()
    except Exception as e:
        print(f"Transcription error: {e}")
        return ""