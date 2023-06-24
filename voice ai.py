engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

   
    speak("I am your friend. Please tell me how may I help you")
     
   
def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='EN-UN')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        speak("say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:

        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'what time is it' in query:
         now = datetime.datetime.now()
         print("It's " + now.strftime("%H:%M:%S"))

        elif "camera" in query or " photo" in query:
          ec.capture(0, "Jarvis Camera ", "img.jpg")


        elif 'who made you' in query:
             speak("i have created by Nisanth")

        elif " i love you" in query:
            speak(" As an AI language model, I'm not capable of romantic love or feelings. However, I'm here to assist you with any questions or tasks you have. How can I assist you today?")
        
        elif "how are you" in query:
            speak("I'm fine, how are you sir") 

        elif "good" in query or "fine" in query:
            speak(" ok sir")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
 
        elif 'fine' in query :
            speak("It's good to know that your fine")


        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("youtube is opened sir")

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("google is opened sir")

        elif 'open chrome' in query:
            webbrowser.open("chrome.com")
            speak("chrome is opened sir")

        elif 'open amazon' in query:
             webbrowser.open("www.amazon.com")
             speak("amazon is opened  sir")

        elif 'open portal' in query:
             webbrowser.open("xyz.com")
             speak("portal is opened sir")

        elif 'open insta' in query:
             webbrowser.open("www.instagram.com/_n.i.s.a.n.t.h_/")

        elif 'open aadhar card downloader' in query:
             webbrowser.open("uidai.gov.in/en/")
             speak("downloader is opened sir")

        elif 'open ration card downloader' in query:
             webbrowser.open("www.tnpds.gov.in")
             speak("downloader is opened sir")

        elif 'play music' in query or "play song" in query:
            speak("Here you go with music")
            # music_dir = "G:\\Song"
            music_dir = "C:\\Users\HP\Videos"
            songs = os.listdir(music_dir)
            print(songs)   
            random = os.startfile(os.path.join(music_dir, songs[1]))





       













        elif 'clear' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")
 
        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()

        elif 'lock window' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call(["shutdown", "/s"])

