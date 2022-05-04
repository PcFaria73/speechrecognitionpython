import speech_recognition as sr
rec = sr.Recognizer()
#print(sr.Microphone().list_microphone_names())

with sr.Microphone(1) as mic:
    rec.adjust_for_ambient_noise(mic)
    print("You can talk now. I'm listening!")
    audio = rec.listen(mic)
    text = rec.recognize_google(audio, language= "pt-BR")
    print(text)

