import s  as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Calibrating for background noise... please wait")
    recognizer.adjust_for_ambient_noise(source, duration=1)
    print("🎙️ Speak something")
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio, language="en-US")
    print("📝 You said:", text)
except sr.UnknownValueError:
    print("😕 Could not understand audio")
except sr.RequestError as e:
    print("❌ unavailable:", e)