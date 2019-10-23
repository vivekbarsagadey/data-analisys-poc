import pyttsx3

eng_message = "Hello Sir, Welcome to whiz It services, Please let me know, How can i help you."
engine = pyttsx3.init()
engine.setProperty('rate', 120)
engine.say(eng_message)
engine.runAndWait()
