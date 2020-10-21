# download PyAudio from here alt+click  (https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) 
import pyttsx3 #Listening function 
import datetime 
import speech_recognition as sr #recognize speech (pip install speechrecognition)
import cheese
import wikipedia
import webbrowser
import os



engine = pyttsx3.init('sapi5')  # for linux use Kaldi(sudo apt install kaldi). # windows inbuild listening function.
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) 


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():                                             #Wishes me according to time 
    hour = int(datetime.datetime.now().hour)
    if hour >  0 and hour < 12:
        speak("Good Morning!Mr Harman")            #24 hour clock

    elif hour > 12 and hour < 18:
        speak("Good afternoon! Mr Harman")

    else:
        speak("Good evening!Mr Harman")

    speak("I am Jarvis . Please tell me how may I help you")


def takeCommand() :
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Fast I am Listening...............")
        speak("speak up I am listening")
        r.pause_threshold = 0.8
        r.energy_threshold = 150
        audio = r.listen(source)

    try:                        # it is often us
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please ..........")
        speak("Say that again please")
        return "None"

    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching in wikipidea please wait Mr Singh')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")

        elif 'play music' in query:
            amzmsic = ("https://music.amazon.in/my/songs")
            webbrowser.open(amzmsic)

        elif 'open google' in query:
            chromepath = ("https://google.com")
            webbrowser.open(chromepath)

        elif 'open amazon music' in query:
            am = (
                "https://music.amazon.in/home?ref=dm_ws_lnd_pm_listn_pm_75c19497-1ddb-4ee0-b8c7-5a5c72387c3e")
            os.startfile(am)

        elif 'open prime videos' in query:
            pv = (
                "https://www.primevideo.com/?ref_=dvm_pds_amz_in_as_s_g_brand27|m_4mEHKPKZc_c386559716835")
            webbrowser.open(pv)

        elif 'show me vampire diaries' in query:
            vamdia = (
                "https://www.primevideo.com/detail/0HOK2IOF5E6RFUO8LL6L4LAW3W/ref=atv_hm_hom_c_8pZiqd_2_1")
            webbrowser.open(vamdia)

        elif 'show khatron ke khiladi' in query:
            kkk = ("https://www.voot.com/shows/khatron-ke-khiladi-made-in-india/308030")
            webbrowser.open(kkk)

        elif 'show naagin' in query:
            nag = ("https://www.voot.com/shows/naagin")
            webbrowser.open(nag)

        elif 'show live tv' in query:
            tasky = ("https://watch.tatasky.com/")
            webbrowser.open(tasky)

        elif 'I love you' in query:
            ily = ("Well ! i am a machine but , I love you too")
            speak(ily)
            print(ily)

        elif 'what is your name' in query:
            wyn = ("I am Jarvis ! Mr Harman Singh created me")
            speak(wyn)
            print(wyn)

        elif 'who created you' in query:
            wcu = ("Mr Harman Singh created me , and I am a child of him")
            speak(wcu)
            print(wcu)

        elif 'thank you' in query:
            ty = ("Welcome, its my pleasure to hear ")
            speak(ty)
            print(ty)

        elif 'I am sad today' in query:
            iats = ("don\'t worry , every thing will be alright")
            speak(iats)
            print(iats)

        elif 'I am so happy today' in query:
            Iasht = ("Nice to hear that")

        elif 'open spotify' in query:
            spot = ("https://open.spotify.com/")
            webbrowser.open(spot)

        elif 'open netflix' in query:
            nfx = ("https://www.netflix.com/in/")
            webbrowser.open(nfx
            )
        elif 'open snapchat' in query:
            snch = ("https://accounts.snapchat.com/accounts/login?continue=https%3A%2F%2Faccounts.snapchat.com%2Faccounts%2Fwelcome")
            webbrowser.open(snch)

        elif 'play movies' in query:
            moviesdir = (r"F:\MUSIC.VIDEOS.MOVIES\movies\HIGH QUALITY")
            os.startfile(moviesdir)

        elif 'shutup' in query:
            stprkts = (
                "As you say , I will stop talking to you , till the time you won't call me , and I will not tolerate this rude behaviour")
            speak(stprkts)
            print(stprkts)
            exit()

        elif 'shut up' in query:
            shup = ("As you say , I will stop talking to you , till the time you won't call me , and I will not tolerate this rude behaviour")
            speak(shup)
            print(shup)
            exit()

        elif 'stop' in query:
            stpss = (
                "Bye , will talk with each other later, thank you for using me")
            speak(stpss)
            print(stpss)
            exit()

        elif 'exit' in query:
            stpsrk = ("Bye , thank you for using me")
            speak(stpsrk)
            print(stpsrk)
            exit()
