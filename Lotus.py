'''                         LOTUS
She is a Virtual assistant and has a Command Line Interface(A GUI can also be created
using tkinter module).
She will help you carry out day to day tasks such as listening to music, opening apps, surfing the web etc..'''

import pyttsx3
import speech_recognition as sr
import datetime
import calendar
import time
import shutil
import mpg123
import wikipedia
import webbrowser
from bs4 import BeautifulSoup
import random
import requests
import wolframalpha
import subprocess
import os

engine = pyttsx3.init()  # Windows user need to use sapi5 as their tts engine
voices = engine.getProperty('voices')
# print(voices[0].id) (For printing voices availaible)
engine.setProperty('voice', voices[31].id)

date_calendar = ('what time is it', 'what is the date', 'show me the calendar', 'tell  me the date')

greet = {
    'hello lotus' : 'Hello Master. How may I assist you?',
    'hi lotus' : 'Hey There! What can I do for you?',
    'ok lotus' : 'Solve a math problem, search for something or need to go somewhere. I can do that for you.',
    'hey lotus' : 'Listening...'
}

ques = {
    'who are you' : 'I am Lotus. Your on the Go Virtual Assistant',
    'what are you' : 'I am a virtual assistant, written and developed in python 3.',
    'what are your hobbies' : 'Solving your queries, That\'s it!!'
}

def speak(audio):
    ''' Function for Taking audio as strings and speak them'''
    engine.say(audio)
    engine.runAndWait()

def wishMe():  # Greeting Process
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Master")
        print("\nLotus: Good Morning")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Master")
        print("\nLotus: Good Afternoon")

    else:
        speak("Good Evening Master")
        print("\nLotus: Good Evening")

    speak("This is Lotus. Ready to take your Commands.")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source,duration=1)
        # r.energy_threshold=350
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"\nYou said: {query}\n")

    except:
        speak("Sorry, I Didn't Catch that. Say that again please...")
        return "None"
    return query

def quit(prompt):
    if prompt.upper()=='I':
        speak("listening")
    elif prompt.upper()=='Q':
        print("\nLotus : Goodbye Master. See you soon. Have a nice day\n")
        speak("Goodbye Master. See you soon. Have a nice day")
        exit()

if __name__ == "__main__":
    wishMe()
    while True: # Uses while loop to continuously listen to commands

        query = takeCommand().lower()
        for greets in greet.keys():
            if query==greets:
                print("Lotus : " + greet[greets])
                speak(greet[greets])
                interact = input("\nPress 'I' to interact or 'Q' to quit : ") # Interaction Through Keyboard
                quit(interact)

        for questions in ques.keys():
            if query==questions:
                print("Lotus : " + ques[questions])
                speak(ques[questions])
                interact = input("\nPress 'I' to interact or 'Q' to quit : ") # Interaction Through Keyboard
                quit(interact)
                

        # Keywords for performing tasks
        if 'wikipedia' in query: # Searches for any thing on wikipedia
            print("Lotus : Command Confirmed\n")
            speak("Command Confirmed")
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) # Change the sentences according to preferences
            speak("According to Wikipedia")
            print(results)
            speak(results)
            interact = input("\nPress 'I' to interact or 'Q' to quit : ") # Interaction Through Keyboard
            quit(interact)

        elif 'create a ' in query:   # Sets a Reminder for short breaks according to the seconds speacified by user
            speak("Please input your reminder time.")
            reminder_time = int(input("Enter the reminder time (in Secs): ")) # 900 secs = 15 Mins
            speak('Setting up a Reminder.....')
            total_reminds = 1   # No of reminders to be given
            break_reminds = 0
            while (break_reminds<total_reminds):
                speak('Reminder has been successfully set.')
                time.sleep(reminder_time)
                break_reminds = break_reminds + 1
                speak("Time is Up!")
                subprocess.call(['mpg123', "reminder.mp3"])
            interact = input("\nPress 'I' to interact or 'Q' to quit : ") # Interaction Through Keyboard
            quit(interact)

        elif 'open youtube' in query:
            print ("Lotus : Command Confirmed")
            speak("Command Confirmed")
            br = webbrowser.get("Safari")
            br.open("https://www.youtube.com/",new=1)
            interact = input("\nPress 'I' to interact or 'Q' to quit : ") # Interaction Through Keyboard
            quit(interact)

        elif 'open google' in query:
            print ("Lotus : Command Confirmed")
            speak("Command Confirmed")
            br = webbrowser.get("Safari")
            br.open("https://www.google.co.in",new=1)
            interact = input("\nPress 'I' to interact or 'Q' to quit : ") # Interaction Through Keyboard
            quit(interact)

        elif 'calculate' in query: # Can do variety of maths problem
            id = 'YOUR WOLFRAM-ID'
            client = wolframalpha.Client(id)
            indx = query.lower().split().index('calculate')
            ques = query.split()[indx + 1:]
            res = client.query(' '.join(ques))
            answer = next(res.results).text
            speak('Let me give it a try!')
            print(f"Lotus : The Answer is {answer}")
            speak('If my mathematics is correct, then the answer might be ' + answer)
            interact = input("\nPress 'I' to interact or 'Q' to quit : ") # Interaction Through Keyboard
            quit(interact)

        elif 'search for ' in query:
            speak('Directing to Google...')
            ques = query.replace('search for', "")
            webbrowser.get('Safari').open(f'https://www.google.com/search?&q={ques}')
            speak('Search for your query while I am still listening...')
            interact = input("\nPress 'I' to interact or 'Q' to quit : ") # Interaction Through Keyboard
            quit(interact)

        elif "where is " in query:# For Maps and Locations
            query = query.replace('where is', "")
            print(f"Lotus : Hold on Master. I will show you where {query} is.")
            speak (f'Hold on Master. I will show you where {query} is.')
            webbrowser.get('Safari').open(f'https://www.google.nl/maps/place/{query}/')
            interact = input("\nPress 'I' to interact or 'Q' to quit : ") # Interaction Through Keyboard
            quit(interact)

        elif "get me " in query:
            print("Lotus : Here are some top Headlines of the day I found on the web: \n")
            speak("Here are some top Headlines of the day I found on the web")
            os.system("python3 news.py")
            interact = input("\nPress 'I' to interact or 'Q' to quit : ") # Interaction Through Keyboard
            quit(interact)

        elif query in date_calendar: # Calendar includes the current date, time and Calendar

            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            date = datetime.datetime.now().date()
            cal = calendar.TextCalendar(calendar.SUNDAY)
            cal1 = cal.formatmonth(2019, 10) # Requires different month int to display different calendars.
            print(f"DATE --> {date} \nTIME --> {strTime}\n")
            speak(f"Sir, The date is {date}. The clock shows that its currently {strTime}")
            speak('And Here\'s the calendar of this month')
            print(cal1)
            interact = input("\nPress 'I' to interact or 'Q' to quit : ") # Interaction Through Keyboard
            quit(interact)

        elif 'show me the weather in ' in query: # Weather Forecast

            speak('According to Open Weather....')
            query = query.replace('show me the weather in', "")
            api = f'https://api.openweathermap.org/data/2.5/weather?&appid="YOUR OPEN_MAP API KEY without quotes"&q={query}'
            weather_data = requests.get(api).json()
            weather= weather_data['weather'][0]['main']
            desc =  weather_data['weather'][0]['description']
            temperature = weather_data['main']['temp']
            temp2 = int(temperature - 273)
            humid= weather_data['main']['humidity']
            country = weather_data['sys']['country']

            print(f"Weather : {weather}")
            print(f"Description : {desc}")
            print(f"Avg. Temperature : {temp2} (°C)")
            print(f"Humidity : {humid}")
            print(f"Country : {country}") # Can add more info like wind speed, latitude etc..

            speak(f"The weather in {query} shows {weather}. The Average temperature being {temp2} degree celcius")
            interact = input("\nPress 'I' to interact or 'Q' to quit : ") # Interaction Through Keyboard
            quit(interact)

        elif 'play ' in query:
            folder = "/Users/crytek/Music/"
            print("Lotus : Here it is, Enjoy. ")
            speak("Here it is, Enjoy!")
            music = 'NEFFEX' ,'Baller', 'Cold'
            random_music = folder + random.choice(music) + '.mp3' # Using Random module to shuffle and play a new song every time.
            subprocess.call(["/usr/bin/open", '-n', '-a', "/Applications/IINA.app", random_music])  # One can also use mpg123 CL Music player which is a command line Music player
            interact = input("\nPress 'I' to interact or 'Q' to quit : ") # Interaction Through Keyboard
            quit(interact)

        elif 'launch' in query or 'open' in query:
            print("Lotus : Command Confirmed")
            speak("Command Confirmed!")   # Can open multiple apps .
            for i in query:
                if 'whatsapp' in query:
                    subprocess.call(["/usr/bin/open", '-n', '-a', "/Applications/Whatsapp.app"])
                    break
                elif 'photos' in query:
                    subprocess.call(["/usr/bin/open", '-n', '-a', "/Applications/Photos.app"])
                    break
                elif 'terminal' in query:
                    subprocess.call(["/usr/bin/open", '-n', '-a', "/Applications/Utilities/Terminal.app"])
                    break

            interact = input("\nPress 'I' to interact or 'Q' to quit : ") # Interaction Through Keyboard
            quit(interact)


