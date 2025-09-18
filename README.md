# SpeechTextRecognition

This project demonstrates basic Speech-to-Text Recognition and Text-to-Speech conversion in Python.  
It includes two scripts: one for converting text into speech and another for capturing voice input and converting it into text.  
A simple project to explore speech-based AI applications.

## Files
- `speech.py` – Converts text into speech using **gTTS** (Google Text-to-Speech). Saves audio as `welcome.mp3` and plays it.  
- `speech_text.py` – Captures audio from the microphone and converts it into text using **speech_recognition** with Google’s Speech API.  

## Features
- Convert your **voice into text** (Speech → Text).  
- Convert **text into speech** (Text → Speech).  
- Uses `gTTS` and `speech_recognition` libraries.  

## Setup
1. **Install dependencies**
   ```bash
   pip install gtts speechrecognition pyaudio
