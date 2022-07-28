import speech_recognition as sr

r = sr.Recognizer()
lacount = 0
therecount = 0
with sr.Microphone() as source:
    print("Speak Anything: ")
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        lacount = text.count("la")
        therecount = text.count("there")            
            
        print("You said: {}".format(text) + ". You said 'la'" + str(lacount) + "  time(s) and 'there' " + str(therecount) + " time(s)." )
    except: 
        print("Sorry, could not recognize your voice.")