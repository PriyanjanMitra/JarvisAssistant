import win32com.client
import speech_recognition as sr
import os
import webbrowser
import datetime
import csv
from weather import *
from news import *

chatStr = ""
speaker = win32com.client.Dispatch("SAPI.SpVoice")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis"


if __name__ == '__main__':
    print('Welcome to Jarvis A.I')
    speaker.Speak("Jarvis AI")
    while True:
        print("Listening...")
        query = takeCommand()
        sites = [['Google', 'https://www.google.com'], ['Youtube', 'https://www.youtube.com'],
                 ['Facebook', 'https://www.facebook.com/'], ['Instagram Web', 'https://www.instagram.com/'],
                 ['LinkedIn', 'https://www.linkedin.com/'], ['Github', 'https://github.com/'],
                 ['Wikipedia', 'https://www.wikipedia.com'], ['W3Schools', 'https://www.w3schools.com/'],
                 ['StackOverflow', 'https://stackoverflow.com/'],
                 ['GeeksForGeeks', 'https://www.geeksforgeeks.org/'], ['LeetCode', 'https://leetcode.com/'],
                 ['Coursera', 'https://www.coursera.org/'], ['Reddit', 'https://www.reddit.com/'],
                 ['Gmail', 'https://mail.google.com/mail/u/0/#inbox'],
                 ['Google Drive', 'https://drive.google.com/drive/u/0/my-drive'],
                 ['Amazon', 'https://www.amazon.in/'], ['Bard', 'https://bard.google.com/chat'],
                 ['Swiggy', 'https://www.swiggy.com/'], ['Chat G.P.T', 'https://chat.openai.com/'],
                 ['Times Of India', 'https://timesofindia.indiatimes.com/?from=mdr'],
                 ['Library', 'https://libgen.li/'], ['Internet Archive', 'https://archive.org/'],
                 ['DTU', 'http://dtu.ac.in/'], ['Python Website', 'https://www.python.org/'],
                 ['Microsoft', 'https://www.microsoft.com/en-in/'],
                 ['Colab', 'https://colab.research.google.com/?utm_source=scs-index'],
                 ['SBI', 'https://www.onlinesbi.sbi/'], ['Threads', 'https://www.threads.net/login'],
                 ['Simple Flying', 'https://simpleflying.com/'], ['Chess', 'https://www.chess.com/home']]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                speaker.Speak(f"Opening {site[0]}")
                webbrowser.open(site[1])
        apps = [['Word', 'C:/Program Files/Microsoft Office/root/Office16/WINWORD.EXE'],
                ['PowerPoint', 'C:/Program Files/Microsoft Office/root/Office16/POWERPNT.EXE'],
                ['Excel', 'C:/Program Files/Microsoft Office/root/Office16/EXCEL.EXE'],
                ['Spotify', 'C:/Users/priya/AppData/Local/Microsoft/WindowsApps/Spotify.exe'],
                ['Instagram', 'C:/Users/priya/OneDrive/Desktop/Shortcuts/Instagram - Shortcut.lnk'],
                ['Whatsapp', 'C:/Users/priya/OneDrive/Desktop/Shortcuts/WhatsApp - Shortcut.lnk'],
                ['Telegram',
                 'C:/Program Files/WindowsApps/TelegramMessengerLLP.TelegramDesktop_4.9.7.0_x64__t4vj0pshhgkwm'
                 '/Telegram.exe'],
                ['Calculator', 'C:/Users/priya/OneDrive/Desktop/Shortcuts/Calculator - Shortcut.lnk'],
                ['PyCharm', 'D:/PyCharm 2023.2.2/bin/pycharm64.exe'],
                ['VS Code', 'C:/Users/priya/AppData/Local/Programs/Microsoft VS Code/Code.exe'],
                ['OMEN',
                 'C:/Users/priya/AppData/Local/Microsoft/WindowsApps/AD2F1837.OMENCommandCenter_v10z8vjag6ke6/ogh.exe'],
                ['Brave', 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe'],
                ['Edge', 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'],
                ['Settings', 'C:/Users/priya/OneDrive/Desktop/Shortcuts/Settings - Shortcut.lnk'],
                ['Epic Games',
                 'C:/Program Files (x86)/Epic Games/Launcher/Portal/Binaries/Win32/EpicGamesLauncher.exe'],
                ['Vortex', 'D:/Games/Vortex/Vortex.exe'], ['Loot', 'D:/Games/LOOT/LOOT.exe'],
                ['Roblox',
                 'C:/Users/priya/AppData/Local/Roblox/Versions/version-510663c9d33e4fd8/RobloxPlayerBeta.exe --app'],
                ['Skyrim', 'D:/Games/The Elder Scrolls V - Skyrim - Legendary Edition/skse_loader.exe'],
                ['Store', 'C:/Users/priya/OneDrive/Desktop/Shortcuts/Microsoft Store - Shortcut.lnk'],
                ['Discord', 'C:/Users/priya/AppData/Local/Discord/Update.exe --processStart Discord.exe'],
                ['BitTorrent', 'C:/Users/priya/AppData/Roaming/bittorrent/BitTorrent.exe'],
                ['Solitaire', 'C:/Users/priya/OneDrive/Desktop/Shortcuts/Solitaire & Casual Games - Shortcut.lnk'],
                ['One Note', 'C:/Program Files/Microsoft Office/root/Office16/ONENOTE.EXE'],
                ['Mail', 'C:/Users/priya/OneDrive/Desktop/Shortcuts/Mail - Shortcut.lnk'],
                ['Explorer', 'C:/Windows/explorer.exe']]

        for app in apps:
            if f"Open {app[0]}".lower() in query.lower():
                speaker.Speak(f"Opening {app[0]}")
                os.startfile(app[1])

        if "the time".lower() in query.lower():
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speaker.Speak(f"Sir time is {time}")
        if "weather".lower() in query.lower():
            weather = (
                f"The day is {description},the current temperature is {temp_celsius:.2f} degree celsius"
                f" and it currently feels like{feels_like_celsius:.2f} degree celsius and the humidity is"
                f"{humidity} percent and the wind speed is {wind_speed:.2f} m/s "
                f"the maximum temperature is {temp_max_celsius:.2f} degree celsius and the minimum temperature is "
                f"{temp_min_celsius:.2f} degree celsius"
                f"the sun rises at {sunrise_time} and the sun sets at {sunset_time}")
            speaker.Speak(weather)
        if "news".lower() in query.lower():
            news = getNews()
            for i in news:
                speaker.Speak(i)
        if "image search".lower() in query.lower():
            API_KEY = "Your Google Custom Search API"
            SEARCH_ENGINE_ID = "76f2b5a93605e4ddc"
            search_query = query.replace("image search", '')
            url = ('https://www.googleapis.com/customsearch/v1?key=' + API_KEY + '&cx=' + SEARCH_ENGINE_ID + '&q=' +
                   search_query)
            paramsimg = {
                'searchType': 'image'
            }
            response = requests.get(url, params=paramsimg)
            results = response.json()['items']
            speaker.Speak(f"Opening Image")
            webbrowser.open(results[0]['link'])
        if "search".lower() in query.lower():
            API_KEY = "Your Google Custom Search API"
            SEARCH_ENGINE_ID = "76f2b5a93605e4ddc"
            search_query = query.replace("search", '')
            url = ('https://www.googleapis.com/customsearch/v1?key=' + API_KEY + '&cx=' + SEARCH_ENGINE_ID + '&q=' +
                   search_query)
            speaker.Speak(f"Searching")
            response = requests.get(url)
            results = response.json()
            if 'items' in results:
                webbrowser.open(results['items'][0]['link'])
        if "search pdf".lower() in query.lower():
            API_KEY = "Your Google Custom Search API"
            SEARCH_ENGINE_ID = "76f2b5a93605e4ddc"
            search_query = query.replace('search pdf', '')
            url = ('https://www.googleapis.com/customsearch/v1?key=' + API_KEY + '&cx=' + SEARCH_ENGINE_ID + '&q=' +
                   search_query)
            paramspdf = {
                'fileType': 'pdf'
            }
            response = requests.get(url, params=paramspdf)
            results = response.json()['items']
            speaker.Speak(f"Opening PDF")
            webbrowser.open(results[0]['link'])
        if "exit".lower() in query.lower():
            exit()

        if "reset chat".lower() in query.lower():
            chatStr = ""


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User said {query}")
            return query
        except Exception:
            return "Please Repeat"
