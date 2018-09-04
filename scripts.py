import os
import webbrowser
import time
import speech_recognition as sr

def google_speech(text):
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        r.adjust_for_ambient_noise(source)
        notify(text)
        audio = r.listen(source)
    notify("Processing")
    query = ""
    try:
        query = r.recognize_google(audio)
    except:
        return str(query)
    return str(query)


def wit_speech(text):
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        r.adjust_for_ambient_noise(source)
        notify(text)
        audio = r.listen(source)
    notify("Processing")
    query = ""
    try:
        query = r.recognize_wit(audio, key = "PLH4QE6OZW2QUY75VBLT6JJCUAFY24KN")
    except:
        return str(query)
    return str(query)


def notify(command):
    os.system("pkill notify-osd")
    os.system("/usr/lib/x86_64-linux-gnu/notify-osd &")
    os.system("notify-send 'Speech Control' '{}'".format(command))

def youtube():
    notify("Opening youtube.com")
    webbrowser.open("https://www.youtube.com")


def google():
    notify("Opening google.com")
    webbrowser.open("https://www.google.com")


def open_file():
    notify("Open file")
    os.system("xdotool key 'ctrl+O'")


def youtube_search():
    notify("Opening Youtube Search")
    search_for = google_speech("Search youtube for??")
    notify("Searching youtube for " + search_for)
    search_for = search_for.replace(" ", "+")
    web_address = "https://www.youtube.com/results?search_query=" + search_for
    webbrowser.open(web_address)
    

def shuffle_music():
    notify("Shuffle : ON")
    os.system("rhythmbox-client --shuffle")


def open_editor():
    notify("Opening Editor")
    os.system("gedit &")


def save_file():
    notify("Save file")
    os.system("xdotool key 'ctrl+s'")
    

def redo():
    notify("Redo")
    os.system("xdotool key 'ctrl+shift+z'")
    
    
def screenshot():
    notify("Take Screenshot")
    fname = int(time.time())
    os.system("import -window root ~/Pictures/{}.png".format(fname))
    

def undo():
    notify("Undo")
    os.system("xdotool key 'ctrl+z'")
    

def home():
    notify("Open home in terminal")
    os.system("gnome-terminal --working-directory ~/")
    
   
def change_tab():
    notify("Change tab")
    os.system("xdotool key 'alt+Tab'")
    
    
def new_window():
    notify("Open New Window")
    os.system("xdotool key 'ctrl+n'")
    

def search():
    notify("Open search box")
    os.system("xdotool key 'ctrl+f'")
    

def map():
    notify("Open map")
    webbrowser.open("https://maps.google.com")
    

def delete():
    notify("press delete")
    os.system("xdotool key 'Delete'")
    
    
def shutdown():
    notify("Shutdown the computer")
    os.system("shutdown now")
    
    
def bright_up():
    notify("Increase Brightness")
    os.system("xdotool key 'XF86MonBrightnessUp'")
    


def check(phrase, text):
    flag = 0
    if phrase in text:
        index = text.find(phrase)
        text = text[:index - 1]
        flag = 1
    os.system("xdotool type '{}'".format(text))
    return flag


def dictation_mode():
    notify("Starting Dictation mode")
    while(True):
        flag = 0
        text = google_speech("Start Speaking: ")
        exit_phrase = ["off dictation", "stop dictation", "dictation off", "stop voice typing", "stop typing"]
        for phrase in exit_phrase:
            if phrase in text:
                index = text.find(phrase)
                text = text[:index - 1]
                flag = 1
                break
        os.system("xdotool type '{}'".format(text))
        if flag:
            break
    
    
def delete_line():
    notify("Delete line")
    os.system("xdotool key 'ctrl+d'")
    
    
def pause_music():
    notify("Pause Music")
    os.system("rhythmbox-client --pause")
    
    
def caps_off():
    notify("Capslock Off")
    os.system("xdotool key Caps_Lock")
    
    
def open_doc():
    notify("Open documents with file manager")
    os.system("xdg-open ~/Documents/")
    
    
def tell_time():
    notify("Time")
    os.system("echo 'It is ' | espeak -g 10 -a 200")
    os.system("date +%I:%M%p | espeak -g 10 -a 200")
    
    
def paste():
    notify("Paste")
    os.system("xdotool key 'ctrl+v'")
    
    
def bright_down():
    notify("Decrease Brightness")
    os.system("xdotool key 'XF86MonBrightnessDown'")
    
    
def close_tab():
    notify("Close Tab")
    os.system("xdotool key 'ctrl+w'")
    
    
def convert_to_audio():
    notify("Speech to computer generated audio file")
    text = google_speech("Start Speaking: ")
    os.system("echo {} | espeak -a 200".format(text))
    
    
def copy():
    notify("Copy")
    os.system("xdotool key 'ctrl+c'")
    

def tell_year():
    notify("Year")
    os.system("echo 'The year is ' | espeak -a 200")
    os.system("date +%Y | espeak -g 10 -a 200")
    
    
def zoom_out():
    notify("Zoom Out")
    os.system("xdotool key 'ctrl+minus'")
    
    
def weather():
    notify("Weather Search")
    search_for = google_speech("City name?")
    notify("Searching weather for " + search_for)
    search_for = search_for.replace(" ", "+")
    web_address = "https://www.google.com/search?q=weather+" + search_for
    webbrowser.open(web_address)
    
    
def random_song():
    notify("Random Song")
    os.system("rhythmbox-client --shuffle")
    
    
def touchpad():
    notify("Touchpad ON/OFF")
    os.system("xdotool key 'XF86TouchpadToggle'")


def logoff():
    notify("Log Off the computer")
    os.system("xdotool key 'Ctrl+Alt+BackSpace'")
    
    
def tab():
    notify("Press Tab")
    os.system("xdotool key Tab")
    
    
def escape():
    notify("Press Escape")
    os.system("xdotool key Escape")
    

def pic():
    notify("Open pictures in terminal")
    os.system("gnome-terminal --working-directory ~/Pictures/")
        
    
def wiki_search():
    notify("Wikipedia Search")
    search_for = google_speech("Search wikipedia for??")
    notify("Searching wikipedia for " + search_for)
    search_for = search_for.replace(" ", "+")
    web_address = "https://www.wikipedia.org/w/index.php?search=" + search_for
    webbrowser.open(web_address)
    
    
def select_all():
    notify("Select All")
    os.system("xdotool key 'ctrl+a'")
    
    
def tell_day():
    notify("Tell Day")
    os.system("echo 'Today is ' | espeak -a 200")
    os.system("date +%A | espeak -g 10 -a 200")
    
    
def close_window():
    notify("Close Window")
    os.system("xdotool key 'alt+F4'")
    
    
def music_player():
    notify("Open Music Player")
    os.system("rhythmbox-client --pause")
    
    
def whoami():
    notify("Who am i")
    os.system("echo 'You are ' | espeak -a 200")
    os.system("whoami | espeak -a 200")
    
    
def tell_date():
    notify("Tell Date")
    os.system("echo 'Today is ' | espeak -a 200")
    os.system("date +%A%d%B%Y | espeak -g 0 -a 200")
    
    
def play_music():
    notify("Play Music")
    os.system("rhythmbox-client --play")
    
    
def open_pic():
    notify("Open pictures with file manager")
    os.system("xdg-open ~/Pictures/")
    
    
def vol_up():
    notify("Increase Volume")
    os.system("xdotool key XF86AudioRaiseVolume")
    os.system("xdotool key XF86AudioRaiseVolume")
    
    
def open_terminal():
    notify("Open Terminal")
    os.system("gnome-terminal")
    
    
def open_dow():
    notify("Open downloads with file manager")
    os.system("xdg-open ~/Downloads/")
    
    
def mail():
    notify("Open Mail")
    os.system("exo-open --launch MailReader")
    
    
def close_terminal():
    notify("Close Terminal")
    os.system("xdotool key 'ctrl+d'")
    
    
def minimize():
    notify("Minimize")
    os.system("xdotool key 'Ctrl+Alt+0'")
    

def prev_song():
    notify("Previous Song")
    os.system("xdotool key XF86AudioPrev")
    
    
def zoom_reset():
    notify("Zoom Reset")
    os.system("xdotool key 'Ctrl+0'")
    
    
def vol_down():
    notify("Decrease Volume")
    os.system("xdotool key XF86AudioLowerVolume")
    os.system("xdotool key XF86AudioLowerVolume")
    
    
def open_gedit():
    notify("Open gedit")
    os.system("gedit &")
    
    
def take_picture():
    notify("Take Picture")
    os.system("cheese & sleep 2s")
    os.system("xdotool key space")
    
def maximize():
    notify("Maximize")
    os.system("xdotool key 'Ctrl+Alt+5'")
    
    
def zoom_in():
    notify("Zoom In")
    os.system("xdotool key 'ctrl+shift+equal'")
    
    
def enter():
    notify("Press Enter")
    os.system("xdotool key KP_Enter")
    
    
def create_folder():
    notify("Create Folder")
    os.system("xdotool key 'Ctrl+Shift+n'")
    
    
def tell_month():
    notify("Tell Month")
    os.system("echo 'This month is ' | espeak -a 200")
    os.system("date +%B | espeak -g 0 -a 200")
    
    
def mute():
    notify("Mute")
    os.system("xdotool key XF86AudioMute")
    
    
def open_calc():
    notify("Open Calculator")
    os.system("gnome-calculator &")
    
    
def dow():
    notify("Open downloads in terminal")
    os.system("gnome-terminal --working-directory ~/Downloads/")
    
    
def save_as():
    notify("Save as")
    os.system("xdotool key 'ctrl+shift+s'")
    
    
def cut():
    notify("Cut")
    os.system("xdotool key 'ctrl+x'")
    
    
def new_tab():
    notify("New Tab")
    os.system("xdotool key 'ctrl+t'")
    
    
def open_browser():
    notify("Open Browser")
    os.system("exo-open --launch WebBrowser")
    
    
def fullscreen():
    notify("Fullscreen On")
    os.system("xdotool type 'f'")
    
    
def menu():
    notify("Open Menu")
    os.system("xdotool key 'alt+F1'")
    
    
def caps_on():
    notify("Capslock On")
    os.system("xdotool key Caps_Lock")
    
    
def google_search():
    notify("Google Search")
    search_for = google_speech("Search google for??")
    notify("Searching google for " + search_for)
    search_for = search_for.replace(" ", "+")
    web_address = "https://www.google.com/search?q=" + search_for
    webbrowser.open(web_address)
    
    
def open_home():
    notify("Open home with file manager")
    os.system("xdg-open ~/")
    
    
def next_song():
    notify("Next Song")
    os.system("xdotool key XF86AudioNext")
    
    
def actions_menu():
    notify("Action Menu")
    os.system("xdotool key 'alt+F10'")
    
    
def doc():
    notify("Open Documents in terminal")
    os.system("gnome-terminal --working-directory ~/Documents/")
    
    
def open_file_manager():
    notify("Open File Manager")
    os.system("xdg-open ~/")
