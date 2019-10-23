import win32com.client as wincl

eng_message = "Hello Sir, Welcome to whiz It services, Please let me know, How can i help you."
speak = wincl.Dispatch('SAPI.SpVoice')
speak.Speak(eng_message)
