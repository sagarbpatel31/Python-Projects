import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    speak("The Current Time is")
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)

def date():
    speak("The Current Date is ")
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    Date = int(datetime.datetime.now().day)
    speak(Date)
    if month == 1:
        speak("January")
    if month == 2:
        speak("February")
    if month == 3:
        speak("March")
    if month == 4:
        speak("April")
    if month == 5:
        speak("May")
    if month == 6:
        speak("June")
    if month == 7:
        speak("July")
    if month == 8:
        speak("August")
    if month == 9:
        speak("September")
    if month == 10:
        speak("October")
    if month == 11:
        speak("November")
    if month == 12:
        speak("December") 
    speak(year)

def wishme():
    speak("Welcome Back Sir")
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <12:
        speak("Good Morning ")
    elif hour >= 12 and hour <18:
        speak("Good Afternoon ")
    elif hour >= 18 and hour <24:
        speak("Good Evening ")
    else:
        speak("Good night")
    time()
    date()
    speak("Jarvis at your service... Please Tell me how can I help you?")

def takeCommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio=r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language='en-in')
        print(query)
    except Exception as e:
        print(e)
        print("Say that again please......")
        return "None"

    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('email_id','passwd')
    server.sendmail('from email id',to,content)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save("D:\\College\\OTHERS\\Udemy\\AI_Jarvis using Python\\s.png")

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at "+usage)
    battery = psutil.sensors_battery()
    speak("Battery is at ")
    speak(battery.percent)

def joke():
    speak(pyjokes.get_joke())

if __name__ =="__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("Searching....")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences=2)
            print(result)
            speak(result)        
        elif 'send email' in query:
            try:
                speak("What email message you want to send...")
                content=takeCommand()
                to = 'toemailid'
                speak("Sending email.....")
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Unable to send the email")

        elif 'search in chrome' in query:
            speak("What should I Search ?")
            try:
                chromepath = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
                search = takeCommand().lower()
                wb.get(chromepath).open_new_tab(search+'.com')
            except Exception as e:
                print(e)
                
        elif 'play songs' in query:
            songs_dir = "D:\College\Other softwares\Songs"
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir,songs[7]))

        elif 'remember that' in query:
            speak("What should I remember ?")
            data = takeCommand()
            speak("You said to remember that "+data)
            remember = open('data.txt','w')
            remember.write(data)
            remember.close()

        elif 'do you know anything' in query:
            remember = open('data.txt')
            speak("You said to remember that "+remember.read())

        elif 'screenshot' in query:
            screenshot()
            speak("Done")

        elif 'cpu' in query:
            cpu()    

        elif 'joke' in query:
            joke()

        elif 'logout' in query:
            os.system("shutdown -l")
        
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
      
        elif 'restart' in query:
            os.system("shutdown /r /t 1")

        elif 'offline' in query:
            speak("Okay sir Shutting down the system")
            quit()        

        elif 'bye' in query:
            speak("Okay sir Shutting down the system")
            quit()
