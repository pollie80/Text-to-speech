import pyttsx3
from gtts import gTTS #based on https://www.geeksforgeeks.org/convert-text-speech-python/
import os

language = 'en'


if __name__ == '__main__':
    what_to_say = "Hello world"

    engine = pyttsx3.init()
    engine.say(what_to_say)
    engine.runAndWait()

    myobj = gTTS(text=what_to_say, lang=language, slow=False)
    myobj.save("whatissaid.mp3")
    #os.system("mpg321 welcome.mp3") #tells system to run this if u have run "brew install mpg123"
