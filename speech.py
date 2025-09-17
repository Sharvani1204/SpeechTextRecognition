from gtts import gTTS
import os
mytext = 'Hii You are started to Learning Artificial Intelligence and Machine Learning'
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("welcome.mp3")
os.system("start welcome.mp3")
