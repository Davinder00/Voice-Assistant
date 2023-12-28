import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import wikipedia.exceptions
import webbrowser
import os
import requests
import random
import smtplib




engine = pyttsx3.init('sapi5')
# volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
# print (volume)
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150) 


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour =int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Mornig")

    elif hour >= 12 and hour < 18:
        speak('Good Afternoon')
    else: 
        speak('Good Evening')
    
    speak('Hello! i am Batman. How can i help you?')


def takecommands():
    #converts listened input in text format
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 600
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognising...")
        text = r.recognize_google(audio, language='en-in')
        print("You said:", text)
    except Exception as e:
        speak("Sorry, I encountered an error while making the request.")
        return "None"
        
    
    return text
    


def fetch_joke():
    url = 'https://official-joke-api.appspot.com/jokes/random'
    response = requests.get(url)
    data = response.json()
    if 'setup' and 'punchline' in data:
        joke = f"{data['setup']} {data['punchline']}"
        return joke
    else:
        return "Sorry, I couldn't fetch a joke at the moment."
    

def get_weather(location):
    url = f"https://wttr.in/{location.replace(' ', '+')}.txt"
    response = requests.get(url)
    data = response.text
    return data
        
    

def fetch_news():
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "country": "+91",  # Specify the country code for India
        "category": "general",  # Specify the news category (e.g., general, business, technology)
        "apiKey": ""  
    }
    response = requests.get(url, params=params)
    data = response.json()

    articles = data.get('articles', [])

    if articles:
        news_list = []
        for article in articles:
            title = article.get('title')
            description = article.get('description')
            news_list.append(f"{title}: {description}")

        return news_list
    else:
        return "Sorry, I couldn't fetch the news at the moment."
    
    
    
def SendEmail(to, content):
    server= smtplib.SMTP("smtb.gmail.com", 587)
    server.ehlo
    server.starttls()
    server.login("youremail@gmail.com", '***********')
    server.sendmail('singhsanty77@gmail.com', to, content)
    server.close()

def calling(name):
    pass 

 



        

        

if __name__ == "__main__":
    wishme()
    while True:
    # if 1:
        text = takecommands().lower()

        if 'wikipedia' in text:
            speak('searching in wikipedia..')
            text = text.replace("wikipedia", "")
            try:
                results = wikipedia.summary(text, sentences=2)
                speak('According to wikipedia')
                speak(results)
            except wikipedia.exceptions.WikipediaException as e:
                print("Wikipedia search error:", str(e))
                break
            

        elif 'who are you' in text:
            speak("I am Batman. I am a voice assistant. I am on early stages of my development so i can't do much. But i can help you with some simple tasks. Like i can tell you a joke, play music, search something on wikipidea for you.")
            

        elif 'open youtube' in text:
            webbrowser.open('https://www.youtube.com')
            break
            

        elif 'open google' in text:
            webbrowser.open('https://www.google.com')
            break
            

        elif 'play music' in text:
            music_dir = 'E:\\usb_silver\\USB Drive'
            songs = os.listdir(music_dir)
            if songs:
                random_song = random.choice(songs)
                os.startfile(os.path.join(music_dir, random_song))
            else:
                speak('No songs found in the playlist.')
                
            break
            
        
        elif 'tell me a joke' in text:
            joke = fetch_joke()
            speak("sure, here a joke for you..")
            speak(joke)
            break
            

        elif 'top news' in text:
            n = fetch_news()
            speak(n)
            break
        
        elif 'how are you' in text:
            speak("I am absolutly fine sir. Thanks for asking. How may i help you?")


        elif 'send email to Davinder' in text:
            try:
                speak('sure sir! tell me what to write')
                content = takecommands()
                to = 'singh00davinder@gmail.com'
                SendEmail(to, content)
                speak("email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry sir, but email could not be sent at the moment")

        elif 'weather' in text:
            try:
                speak('Please provide the location')
                location = takecommands()
                w = get_weather(location)
                speak(w)
            except Exception as e:
                speak("Sorry, could'nt fetch weather details right now")






        

    
