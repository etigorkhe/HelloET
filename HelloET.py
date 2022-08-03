import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser  #inbilt module
import os
import smtplib

engine= pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):   #take string and speak output
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("Hello i am ET, Please tell me how can i help you")

def takeCommand():
    '''
    takes microphone input from user and returns string output from speech recognation module
    '''

    r = sr.Recognizer()  #will help in audio recognaise (speech recognisation module is used here)
    with sr.Microphone() as source:
        print("Please Speak, I am listening...")
        r.pause_threshold = 1 #help in staying before completing a sentance and giving output
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, Language='en-in')  #recognising audio which we have typed
        print(f"User said:  {query}\n")

    except Exception as e:       #audio not recoganisable then it goes in except
        #print(e)
        print("Not Audible Say that again please..")
        return "None" #none string when there is problem
    return query  #taking audio in the form of query and returning string o/p

def sendEmail(to, content):  #used for sending emails to a perticular email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('etigorkhe@gmail.com', 'password')  #individual password and email of id required which sends email
    server.sendmail('etigorkhe19@gmail.com', to, content) #content send in mail
    server.close()  #closing server after mail is sent



if __name__ == "__main__":
    wishMe()
    while True:
    #if 1:
        #logic for exectuing task
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia please wait...')
            query = query.replace("wikipedia", "")  #search on wikipedia
            results = wikipedia.summary(query,sentences=2) #will reaturn 2 statements from wikipedia
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time right now is {strTime}")

        elif 'open code' in query:
            codePath = "F:\\OneDrive\\Desktop\\Telegram.lnk"
            os.startfile(codePath)

        elif 'email to me' in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = "etigorkhe19@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry not able to sent the email")


