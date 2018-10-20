#import webbrowser
import time
from playsound import playsound
#play sound help link : https://pypi.org/project/playsound/

def pomodoro():

    stop = "n"
    while stop == "n":
        session = raw_input("Session in Minutes: ")
        break_time = raw_input("Break in Minutes: ")
        session = float(session)
        break_time = float(break_time)
        time.sleep(session*60)
        playsound("aud.MP3")
        time.sleep(break_time*60)
        playsound("aud.MP3")
        stop = raw_input("Is it enough? Y/N")
        


pomodoro()