#!/usr/bin/env python
# coding: utf-8

# In[1]:


from translate import Translator
from pynotifier import Notification
import psutil
import turtle
import speech_recognition as sr
import webbrowser as wb
import pyqrcode
import emoji
import wikipedia  
import calendar
from covid import Covid 
from win10toast import ToastNotifier
import time
from datetime import datetime
from datetime import date
import datetime
import pyttsx3
import pyautogui
import os
import subprocess
from tkinter import *
root=Tk()
def wishme() :
    engine = pyttsx3.init()
    engine.say('welcome to chat')
    engine.runAndWait()
    hour = datetime.datetime.now().hour
    if hour>=6 and hour<12 :
        engine = pyttsx3.init()
        engine.say('Good morning.')
        engine.runAndWait()
    elif hour>=12 and hour<18 :
        engine = pyttsx3.init()
        engine.say('Good afternoon.')
        engine.runAndWait()
    elif hour>=18 and hour<24 :
        engine = pyttsx3.init()
        engine.say('Good evening.')
        engine.runAndWait()
    else :
        engine = pyttsx3.init()
        engine.say('Good night')
        engine.runAndWait()

wishme()
def send():
    send="you:"+a.get()
    text.insert(END,"\n"+send)
    if(a.get()=='hi'):
        text.insert(END,"\n" + "Bot:hello")
    elif(a.get()=='hello'):
        text.insert(END,"\n"+ "Bot:hi")
    elif(a.get()=='How are you?'):
        text.insert(END,"\n"+ "Bot:I am fine. How are you?")
    elif(a.get()=='I am fine'):
        text.insert(END,"\n"+ "Bot:Nice to hear that")
    elif(a.get()=='open notepad'):
        os.system('notepad')
        text.insert(END,"\n"+ "Bot:notepad opened ")
    elif(a.get()=='open chrome'):
        os.system('chrome')
        text.insert(END,"\n"+ "Bot:chrome opened")
    elif(a.get()=='open media player'):
        os.system('wmplayer')
        text.insert(END,"\n"+ "Bot:media player opened ")
    elif(a.get()=='open calculator'):
        subprocess.Popen(r'C:\\Windows\\System32\\calc.exe')
        text.insert(END,"\n"+ "Bot:calculator opened ")
    elif(a.get()=='open control panel'):
        subprocess.Popen(r'C:\\Windows\\System32\\control')
        text.insert(END,"\n"+ "Bot:control panel opened ")
    elif(a.get()=='take screenshot'):
        img=pyautogui.screenshot()
        img.save(r"C:\Users\raghava\Desktop\raki.jpg")
        text.insert(END,"\n"+ "Bot:screenshot saved please check once")
    elif(a.get()=='who created you'):
         text.insert(END,"\n"+ "Bot:Created by Rakesh Rohan")
    elif(a.get()=='good morning'):
        text.insert(END,"\n"+ "Bot:good morning")
        engine = pyttsx3.init()
        engine.say('Good morning.')
        engine.runAndWait()
    elif(a.get()=='present time'):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        text.insert(END,"\n"+ f"Bot:time is{current_time}")
    elif(a.get()=='get notification'):
        toaster=ToastNotifier()
        toaster.show_toast('Notification!','redeem you 1000 rupees',threaded=True,icon_path=None,duration=3)
        while toaster.notification_active():
            time.sleep(0.1)
        text.insert(END,"\n"+ "Bot:notification received")
    elif(a.get()=='what is todays date'):
        today = date.today()
        text.insert(END,"\n"+ f"Bot:date is {today}")
    elif(a.get()=='covid information'):
        covid = Covid() 
        india = covid.get_status_by_country_name("india") 
        data ={ 
	            key:india[key] 
	           for key in india.keys() and {'confirmed', 
								'active', 
								'deaths', 
								'recovered'} 
              } 
        text.insert(END,"\n"+ f"Bot:covid info {data} ")
    elif(a.get()=='search vjit websites'):
        try: 
	        from googlesearch import search 
        except ImportError: 
	        text.insert(END,"\n"+ "Bot:module not formed")

# to search 
        query = "vidya jyothi institute of technology"

        for j in search(query, tld="co.in", num=10, stop=10, pause=2): 
	        text.insert(END,"\n"+ f"Bot:vjit sites {j}")
    elif(a.get()=='calendar this month'):
        yy = 2020
        mm = 9
        text.insert(END,"\n"+ f"Bot:month is {calendar.month(yy, mm)}")  
    elif(a.get()=='year calendar'):
        text.insert(END,"\n"+ f"Bot:month is {calendar.calendar(2020, 2, 1, 6)}")
    elif(a.get()=='about india from wikipedia'):
        result = wikipedia.summary("India", sentences = 2) 
        text.insert(END,"\n"+ f"Bot:About India {result}")
    elif(a.get()=='lough please'):
        k=emoji.emojize(":grinning_face_with_big_eyes:")
        text.insert(END,"\n"+ f"Bot:loughing {k}")
    elif(a.get()=='find some emojis'):
        t="\U0001f600"
        b="\N{grinning face}"
        c="\N{slightly smiling face}"
        d="\N{winking face}"
        e="\U0001F606"
        text.insert(END,"\n"+ f"Bot:emojis {t}{b}{c}{d}{e}")
    elif(a.get()=='show qrcode for my link'):
        link="https://rakeshrohanaie.bolgspot.com"
        url=pyqrcode.create(link)
        url.show()
    elif(a.get()=='open python site'):
        webbrowser.open('http://www.python.org')
    elif(a.get()=='open linkedin'):
        text.insert(END,"\n"+ "Bot:opened")
        wb.open("https://www.linkedin.com/")
    elif(a.get()=='open facebook'):
        text.insert(END,"\n"+ "Bot:opened")
        wb.open("https://www.facebook.com/")
    elif(a.get()=='text to speech'):
        from win32com.client import Dispatch
        import tkinter as tk
 
       #speak = Dispatch("SAPI.SpVoice")
        speak = Dispatch("SAPI.SpVoice")
        def talk(x):
	        speak.Speak(x.get('1.0',tk.END))
 
 
        root = tk.Tk()
        root.title("Speak with Python")
        root.geometry("300x300")
        label = tk.Label(root, text="ENTER TEXT BELOW").pack()
        entry = tk.Text(root)
        entry.insert("1.0","Ciao")
        button = tk.Button(root, text="speak", command=lambda : talk(entry))
        button.pack()
        entry.pack()
        entry.focus()
        root.mainloop()
    elif(a.get()=='your favourate hero'):
        from PIL import ImageTk,Image  
        root = Tk()  
        canvas = Canvas(root, width = 1000, height = 1000)  
        canvas.pack()  
        img = ImageTk.PhotoImage(Image.open("pawan-kalyan.jpeg"))  
        canvas.create_image(40, 40, anchor=NW, image=img) 
        root.mainloop() 
    elif(a.get()=='can you draw square'):
        text.insert(END,"\n"+ "Bot:ok i will draw")
        s=turtle.getscreen()
        t = turtle.Turtle()
        t.fd(100)
        t.rt(90)
        t.fd(100)
        t.rt(90)
        t.fd(100)
        t.rt(90)
        t.fd(100)
    elif(a.get()=='can you draw rectangle'):
        text.insert(END,"\n"+ "Bot:ok i will draw")
        s=turtle.getscreen()
        t = turtle.Turtle()
        t.fd(100)
        t.rt(90)
        t.fd(80)
        t.rt(90)
        t.fd(100)
        t.rt(90)
        t.fd(80)
    elif(a.get()=='show my battery perrcentage'):
        battery=psutil.sensors_battery()
        percent=battery.percent
        Notification("Battery percentage",str(percent)+"%percent Remaining",duration=10).send()
        text.insert(END,"\n"+ "Bot:yeah done once check system notifications")
    elif(a.get()=='english to telugu i love you'):
        translator=Translator(from_lang='english',to_lang='Telugu')
        result=translator.translate('iloveyou')
        text.insert(END,"\n"+ f"Bot:yeah done {result}")
    elif(a.get()=="telugu to english nanu ninnu pramistunnannu"):
        translator=Translator(from_lang='Telugu',to_lang='english')
        result=translator.translate('నేను నిన్ను ప్రేమిస్తున్నాను')
        text.insert(END,"\n"+ f"Bot:yeah done {result}")
    elif(a.get()=="spanish to english te amo"):
        translator=Translator(from_lang='spanish',to_lang='english')
        result=translator.translate('te amo')
        text.insert(END,"\n"+ f"Bot:yeah done {result}")
    elif(a.get()=='english to hindi i love you'):
        translator=Translator(from_lang='english',to_lang='hindi')
        result=translator.translate('iloveyou')
        text.insert(END,"\n"+ f"Bot:yeah done {result}")
    elif(a.get()=="quatation on love"):
        engine = pyttsx3.init()
        engine.say('Life without love is like a tree without blossoms or fruit')
        engine.runAndWait()
        text.insert(END,"\n"+ f"Bot:yeah done completed")
    elif(a.get()=='quatation on life from any telugu movie'):
        engine = pyttsx3.init()
        engine.say('jeevitham lo manam korukune prathi soukaryam venuka oka mini yudame untundhi')
        engine.runAndWait()
        text.insert(END,"\n"+ f"Bot:yeah done completed")
    elif(a.get()=='ipl score'):
        import tkinter as tk
        from PIL import ImageTk, Image
        import os
        from bs4 import BeautifulSoup
        import urllib.request
        score_page = 'http://static.cricinfo.com/rss/livescores.xml'    
        page = urllib.request.urlopen(score_page)
        soup = BeautifulSoup(page, 'html.parser')
        result = soup.find_all('description') 

        ls=[]
        for match in result:
            ls.append(match.get_text())
        def score():
            T.insert(tk.END,ls)
    
        def clear():
            T.delete(1.0,tk.END)
    
    
        root = tk.Toplevel()
        root.geometry('1200x675')
        img = ImageTk.PhotoImage(Image.open("mi.JPG"))
        panel = tk.Label(root, image = img)
        panel.place(x=0,y=0)
        T=tk.Text(root)
        T.place(x=30,y=250,height=250,width=300)
        l=tk.Label(root,text="LIVE SCORE",fg="white",bg="black")
        l.place(x=30,y=400,height=100,width=300)
        b1=tk.Button(root,text="Score",bg="black",fg="red",command=score)
        b1.place(x=800,y=200,height=100,width=250)
        b2=tk.Button(root,text="Clear",bg="black",fg="red",command=clear)
        b2.place(x=800,y=400,height=100,width=250)
        root.mainloop()
        
    else:
        text.insert(END,"\n"+ "Bot:I didn't get it ")
text=Text(root,bg='white')
text.grid(row=0,column=0,columnspan=2)
a=Entry(root,width=80)
send=Button(root,text='Send',bg='white',width=20,command=send).grid(row=1,column=1)
a.grid(row=1,column=0)
root.title('simple chatbot')
root.mainloop()


# In[ ]:




