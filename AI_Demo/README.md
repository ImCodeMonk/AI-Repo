# AI Text to Speech Demo (ElevenLabs)

This project demonstrates how to generate and play AI voice audio using the ElevenLabs Text-to-Speech API in Python.

The script sends text to the ElevenLabs API and plays the generated speech using pygame.

## Features
- Convert text into AI-generated voice
- Uses ElevenLabs TTS API
- Plays audio directly using pygame
- Simple Python implementation

## Requirements

Install dependencies:

pip install requests pygame

## Setup

1. Get your API key from ElevenLabs.
2. Replace the placeholder API key in the code:

ELEVENLABS_API_KEY = "YOUR_API_KEY"

3. Run the script.

## Run the Project

python main.py

## Example Output

The program will:
1. Send text to ElevenLabs API
2. Receive an MP3 audio response
3. Play the generated voice using pygame

## Project Structure
ai-voice-demo
│
├── main.py
├── README.md
└── .gitignore


## Security Note

Never commit your real API keys to GitHub.  
Always store API keys in environment variables or a `.env` file.

## Future Improvements

- Add microphone input
- Build a chatbot voice assistant
- Add a GUI interface
- Integrate with OpenAI or LLM models

## Author

Created by Shubham