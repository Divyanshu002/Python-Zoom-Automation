# Library

import os
import time
import schedule
import webbrowser

print("Script Running")


# Functions

def Zoom_meeting():
    print("Starting Zoom")
    os.startfile("")
    # Add zoom location between the ("C:\Users\Divyanshu\AppData\Roaming\Zoom\bin\Zoom.exe")


def open_link1(link1):
    webbrowser.open(link1)


def First_meeting():
    print("Joining First Meeting")
    open_link1("")
    # Add first meeting link between the ("")


def open_link2(link2):
    webbrowser.open(link2)


def Second_meeting():
    print("Joining Second Meeting")
    open_link2("")
    # Add second meeting link between the ("")


# Scheduling

schedule.every().day.at("00:00").do(Zoom_meeting)  # Zoom launch time

schedule.every().day.at("00:00").do(First_meeting)  # First meeting join time

schedule.every().day.at("00:00").do(Second_meeting)  # Second meeting join time


# Loop

while True:
    schedule.run_pending()
    time.sleep(1)
