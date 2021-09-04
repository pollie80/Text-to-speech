import pyttsx3

engine = pyttsx3.init()

if __name__ == '__main__':
    what_to_say = "Hello world"
    engine.say(what_to_say)
    engine.runAndWait()