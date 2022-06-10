import pyttsx3

def say_text_as_audio(text: str):
    tts = pyttsx3.init()
    voices = tts.getProperty('voices')
    # Задать голос по умолчанию
    tts.setProperty('voice', 'ru')
    tts.say(text)
    tts.runAndWait()