import requests, io, pygame

ELEVENLABS_API_KEY = "[ENCRYPTION_KEY]"
VOICE_ID = "21m00Tcm4TlvDq8ikWAM"
INPUT_TEXT = """
Hello there! I am an artificial intelligence(AI), and this is a demonstration of the 
Eleven Labs text-to-speech integration. The weather is quite nice today, and I am 
ready to help you with your next big project.
"""

# --- DO NOT EDIT BELOW THIS LINE ---
audio = requests.post(
    f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}",
    headers={"xi-api-key": ELEVENLABS_API_KEY, "Content-Type": "application/json"},
    json={"text": INPUT_TEXT, "model_id": "eleven_turbo_v2_5", "voice_settings": {"stability": 0.5, "similarity_boost": 0.5}}
)
if audio.status_code == 200:
    pygame.mixer.init()
    pygame.mixer.music.load(io.BytesIO(audio.content), "mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.wait(100)
else:
    print(f"Error {audio.status_code}: {audio.text}")
