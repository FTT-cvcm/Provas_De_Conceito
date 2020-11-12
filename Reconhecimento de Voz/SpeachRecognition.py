import speech_recognition as sr;

r = sr.Recognizer();

with sr.Microphone() as source:
    print("Diga algo!")
    audio = r.listen(source)
    
    try:
        print("Você disse: " + r.recognize_google(audio, language="pt-BR") + " - By Api:Google")
    except sr.UnknownValueError:
        print("Não entendi...")
    except sr.RequestError as e:
        print("Erro na chamada da API da Google: {0}".format(e))
    