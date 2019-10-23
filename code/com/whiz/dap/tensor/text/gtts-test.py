"""

this is GTTS lib for Google Text-to-Speech

"""

from gtts import gTTS

eng_message = "Hello Sir, Welcome to whiz It services, Please let me know, How can i help you."
hindi_message = "हेलो सर, वेलकम टू व्हाट इट सर्विसेज, प्लीज मुझे बताएं, मैं आपकी कैसे मदद कर सकता हूं"

model = gTTS(text=eng_message, slow=False, lang='en')
model.save('hello-eng.mp3')

model = gTTS(text=hindi_message, slow=False, lang='hi')
model.save('hello-hin.mp3')
