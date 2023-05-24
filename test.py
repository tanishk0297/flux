import datetime
from email import message
import webbrowser
from numpy import tile
import pyttsx3
import speech_recognition as sr
import requests
from bs4 import BeautifulSoup
import os
import pyautogui
import random
from plyer import notification
from pygame import mixer
import speedtest
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from Calculatenumbers import speak
from Jarvis_main import alarm
from frontend import Ui_MainWindow
import sys

from game import takeCommand

for i in range(3):
    a = input("Enter Password to open Jarvis :- ")
    pw_file = open("password.txt","r")
    pw = pw_file.read()
    pw_file.close()
    if (a==pw):
        print("WELCOME SIR ! PLZ SPEAK [WAKE UP] TO LOAD ME UP")
        break
    elif (i==2 and a!=pw):
        exit()

    elif (a!=pw):
        print("Try Again")

from INTRO import play_gif
play_gif

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)
class MainThread(QThread):
    def __init__(self):
         super (MainThread, self).__init__()
    def run(self):
        self.TaskExecution()
    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    
    def alarm(self):
                timehere = open("Alarmtext.txt","a")
                timehere.write(self.query)
                timehere.close()
                os.startfile("alarm.py")
    def takecommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening...")
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source) 
        # audio = r.listen(source, timeout=5, phrase_time_limit=8)
        try:
            print("Recognizing...")
            query=r.recognize_google (audio, language='en-in')
            print(f"user said: {query}")
            query = self.query.lower()
        except Exception as e:
            # speak ("Say that again please...")
            return "none"
        
        return query
    def TaskExecution(self):
                while True:
                    self.query = self.takecommand().lower()
                    if "wake up" in self.query:
                        from GreetMe import greetMe
                        greetMe()

                        while True:
                            self.query = self.takecommand().lower()
                            if "go to sleep" in self.query:
                                speak("Ok sir , You can call me anytime")
                                break 
                            
                            #################### JARVIS: THe Trilogy 2.0 #####################

                            elif "change password" in self.query:
                                speak("What's the new password")
                                new_pw = input("Enter the new password\n")
                                new_password = open("password.txt","w")
                                new_password.write(new_pw)
                                new_password.close()
                                speak("Done sir")
                                speak(f"Your new password is{new_pw}")

                            elif "schedule my day" in self.query:
                                tasks = [] #Empty list 
                                speak("Do you want to clear old tasks (Plz speak YES or NO)")
                                self.query = self.takecommand().lower()
                                if "yes" in self.self.query:
                                    file = open("tasks.txt","w")
                                    file.write(f"")
                                    file.close()
                                    no_tasks = int(input("Enter the no. of tasks :- "))
                                    i = 0
                                    for i in range(no_tasks):
                                        tasks.append(input("Enter the task :- "))
                                        file = open("tasks.txt","a")
                                        file.write(f"{i}. {tasks[i]}\n")
                                        file.close()
                                elif "no" in self.query:
                                    i = 0
                                    no_tasks = int(input("Enter the no. of tasks :- "))
                                    for i in range(no_tasks):
                                        tasks.append(input("Enter the task :- "))
                                        file = open("tasks.txt","a")
                                        file.write(f"{i}. {tasks[i]}\n")
                                        file.close()

                            elif "show my schedule" in self.query:
                                file = open("tasks.txt","r")
                                content = file.read()
                                file.close()
                                mixer.init()
                                mixer.music.load("notification.mp3")
                                mixer.music.play()
                                notification.notify(
                                    title = "My schedule :-",
                                    message = content,
                                    timeout = 15
                                )

                            elif "focus mode" in self.query:
                                a = int(input("Are you sure that you want to enter focus mode :- [1 for YES / 2 for NO "))
                                if (a==1):
                                    speak("Entering the focus mode....")
                                    os.startfile("C:\\Users\\HP\\OneDrive\\Desktop\\jarvis\\Jarvis_Final-20221202T081334Z-001\\Jarvis_Final\\FocusMode.py")
                                    exit()

                                
                                else:
                                    pass

                            elif "show my focus" in self.query:
                                from FocusGraph import focus_graph
                                focus_graph()

                            elif "translate" in self.query:
                                from Translator import translategl
                                self.query = self.query.replace("jarvis","")
                                self.query = self.query.replace("translate","")
                                translategl(self.query)

                            


                            elif "open" in self.query:   #EASY METHOD
                                self.query = self.query.replace("open","")
                                self.query = self.query.replace("jarvis","")
                                pyautogui.press("super")
                                pyautogui.typewrite(self.query)
                                pyautogui.sleep(2)
                                pyautogui.press("enter")                       
                                
                            elif "internet speed" in self.query:
                                wifi  = speedtest.Speedtest()
                                upload_net = wifi.upload()/1048576         #Megabyte = 1024*1024 Bytes
                                download_net = wifi.download()/1048576
                                print("Wifi Upload Speed is", upload_net)
                                print("Wifi download speed is ",download_net)
                                speak(f"Wifi download speed is {download_net}")
                                speak(f"Wifi Upload speed is {upload_net}")
                                

                            elif "ipl score" in self.query:
                                from plyer import notification  #pip install plyer
                                import requests #pip install requests
                                from bs4 import BeautifulSoup #pip install bs4
                                url = "https://www.cricbuzz.com/"
                                page = requests.get(url)
                                soup = BeautifulSoup(page.text,"html.parser")
                                team1 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
                                team2 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
                                team1_score = soup.find_all(class_ = "cb-ovr-flo")[8].get_text()
                                team2_score = soup.find_all(class_ = "cb-ovr-flo")[10].get_text()

                                a = print(f"{team1} : {team1_score}")
                                b = print(f"{team2} : {team2_score}")

                                notification.notify(
                                    title = "IPL SCORE :- ",
                                    message = f"{team1} : {team1_score}\n {team2} : {team2_score}",
                                    timeout = 15
                                )
                            
                            elif "play a game" in self.query:
                                from game import game_play
                                game_play()

                            elif "screenshot" in self.query:
                                import pyautogui #pip install pyautogui
                                im = pyautogui.screenshot()
                                im.save("ss.jpg")

                            elif "click my photo" in self.query:
                                pyautogui.press("super")
                                pyautogui.typewrite("camera")
                                pyautogui.press("enter")
                                pyautogui.sleep(2)
                                speak("SMILE")
                                pyautogui.press("enter")

                            
                            

                            ############################################################
                            elif "hello" in self.query:
                                speak("Hello sir, how are you ?")
                            elif "i am fine" in self.query:
                                speak("that's great, sir")
                            elif "how are you" in self.query:
                                speak("Perfect, sir")
                            elif "thank you" in self.query:
                                speak("you are welcome, sir")
                            
                            elif "tired" in self.query:
                                speak("Playing your favourite songs, sir")
                                a = (1,2,3)
                                b = random.choice(a)
                                if b==1:
                                    webbrowser.open("https://www.youtube.com/watch?v=E3jOYQGu1uw&t=1246s&ab_channel=scientificoder")
                                

                            elif "pause" in self.query:
                                pyautogui.press("k")
                                speak("video paused")
                            elif "play" in self.query:
                                pyautogui.press("k")
                                speak("video played")
                            elif "mute" in self.query:
                                pyautogui.press("m")
                                speak("video muted")
                            


                            elif "volume up" in self.query:
                                from keyboard import volumeup
                                speak("Turning volume up,sir")
                                volumeup()
                            elif "volume down" in self.query:
                                from keyboard import volumedown
                                speak("Turning volume down, sir")
                                volumedown()

                            elif "open" in self.query:
                                from Dictapp import openappweb
                                openappweb(self.query)
                            elif "close" in self.query:
                                from Dictapp import closeappweb
                                closeappweb(self.query)


                            elif "google" in self.query:
                                from SearchNow import searchGoogle
                                searchGoogle(self.query)
                            elif "youtube" in self.query:
                                from SearchNow import searchYoutube
                                searchYoutube(self.query)
                            elif "wikipedia" in self.query:
                                from SearchNow import searchWikipedia
                                searchWikipedia(self.query)

                            
                            elif "news" in self.query:
                                from NewsRead import latestnews
                                latestnews()

                            elif "calculate" in self.query:
                                from Calculatenumbers import WolfRamAlpha
                                from Calculatenumbers import Calc
                                self.query = self.query.replace("calculate","")
                                self.query = self.query.replace("jarvis","")
                                Calc(self.query)

                            elif "whatsapp" in self.query:
                                from Whatsapp import sendMessage
                                sendMessage()

                            

                            elif "temperature" in self.query:
                                search = "temperature in "
                                url = f"https://www.google.com/search?q={search}"
                                r  = requests.get(url)
                                data = BeautifulSoup(r.text,"html.parser")
                                temp = data.find("div", class_ = "BNeawe").text
                                speak(f"current{search} is {temp}")
                            elif "weather" in self.query:
                                search = "temperature in bhopal"
                                url = f"https://www.google.com/search?q={search}"
                                r  = requests.get(url)
                                data = BeautifulSoup(r.text,"html.parser")
                                temp = data.find("div", class_ = "BNeawe").text
                                speak(f"current{search} is {temp}")

                            elif "set an alarm" in self.query:
                                print("input time example:- 10 and 10 and 10")
                                speak("Set the time")
                                a = input("Please tell the time :- ")
                                alarm(a)
                                speak("Done,sir")
                                    
                            elif "the time" in self.query:
                                strTime = datetime.datetime.now().strftime("%H:%M")    
                                speak(f"Sir, the time is {strTime}")
                            elif "finally sleep" in self.query:
                                speak("Going to sleep,sir")
                                exit()

                            elif "remember that" in self.query:
                                rememberMessage = self.query.replace("remember that","")
                                rememberMessage = self.query.replace("jarvis","")
                                speak("You told me to remember that"+rememberMessage)
                                remember = open("Remember.txt","a")
                                remember.write(rememberMessage)
                                remember.close()
                            elif "what do you remember" in self.query:
                                remember = open("Remember.txt","r")
                                speak("You told me to remember that" + remember.read())

                            elif "shutdown system" in self.query:
                                speak("Are You sure you want to shutdown")
                                shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                                if shutdown == "yes":
                                    os.system("shutdown /s /t 1")

                                elif shutdown == "no":
                                    break

startExecution = MainThread()
class Main (QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui= Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask) 
        self.ui.pushButton_3.clicked.connect(self.close)
    def startTask(self):
        self.ui.movie = QtGui.QMovie("C:\\Users\\HP\\OneDrive\\Desktop\\jarvis\\Jarvis_Final-20221202T081334Z-001\\Jarvis_Final\\Black_Template.jpg")
        self.ui.label.setMovie (self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("C:\\Users\\HP\\OneDrive\\Desktop\\jarvis\\Jarvis_Final-20221202T081334Z-001\\Jarvis_Final\\Iron_Template_1.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("C:\\Users\\HP\\OneDrive\\Desktop\\jarvis\\Jarvis_Final-20221202T081334Z-001\\Jarvis_Final\\Jarvis_Gui (1).gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self) 
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()
    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)
app = QApplication (sys.argv)
test = Main()
test.show()
exit (app.exec_())


                                


                
    