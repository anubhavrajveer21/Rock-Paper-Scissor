import random
import json
import torch
from Brain import NeuralNet
from NeuralNetwork import bag_of_words ,tokenize
import requests
import datetime
from bs4 import BeautifulSoup
from pywebio import *

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
with open("intents.json",'r') as json_data:
    intents = json.load(json_data)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                
FILE = "TrainData.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNet(input_size,hidden_size,output_size).to(device)
model.load_state_dict(model_state)
model.eval()

#---------------------------------------------

from Listen import Listen
from Speak import Say
from Task import InputExecution
from Task import NonInputExecution

def Wish():
    # print("Note : Before Starting Jarvis, Open Train.py for not getting error")
    # print("Checking Drivers....")
    # print("Checking Network Connection...")
    # print("Updating Drivers....")
    # print("Please wait Sir....")
    search = f"temperature in delhi"
    wish_time = datetime.datetime.now().strftime("%H:%M")
    wish_day = datetime.datetime.now().strftime("%A")
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    temp = data.find("div", class_="BNeawe").text
    
    # Say("Let Me to introduce myself , I am Jarvis a virtual artificial intelligence i can do many tasks like tell you about a famous person, Automate google chrome, youtube, windows and many more")
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        Say("Good Morning Sir")

    elif hour>=12 and hour<18:
        Say("Good Afternoon Sir")

    else:
        Say("Good Evening Sir")

    Say(f"Sir Today is {wish_day} Its {wish_time} and the temperature is {temp} ")
    
def Main():

    sentence = Listen.Listen()
    result = str(sentence)

    if sentence == "you need a break":
        Say("Ok Sir i am going to sleep, you can call me anytime just say Wake Up")
        exit()
        
    if sentence == "bye":
        Say("Bye")
        exit()
        
    if sentence == "wake up":
        print("HFeature will Come Soon!")

    sentence = tokenize(sentence)
    X = bag_of_words(sentence,all_words)
    X = X.reshape(1,X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)

    _ , predicted = torch.max(output,dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output,dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                reply = random.choice(intent["responses"])

                if "time" in reply:
                    NonInputExecution(reply)

                elif "date" in reply:
                    NonInputExecution(reply)

                elif "day" in reply:
                    NonInputExecution(reply)

                elif "wikipedia" in reply:
                    InputExecution(reply,sentence)
                    
                elif "Summary" in reply:
                    InputExecution(reply,sentence)
                    
                elif "google search" in reply:
                    InputExecution(reply,sentence)
                    
                elif "youtube search" in reply:
                    InputExecution(reply,sentence)
                    
                elif "download youtube" in reply:
                    InputExecution(reply,sentence)
                    
                elif "corona virus" in reply:
                    NonInputExecution(reply)
                    
                elif "google" in reply:
                    NonInputExecution(reply)
                    
                elif "screenshot" in reply:
                    NonInputExecution(reply)
                
                elif "calculate" in reply:
                    NonInputExecution(reply)
                    
                elif "location" in reply:
                    NonInputExecution(reply)
                    
                elif "joke" in reply:
                    NonInputExecution(reply)
                    
                elif "youtube" in reply:
                    NonInputExecution(reply)
                    
                elif "opening code" in reply:
                    NonInputExecution(reply)
                     
                elif "closing code" in reply:
                    NonInputExecution(reply)
                    
                elif "opening notepad" in reply:
                    NonInputExecution(reply)
                    
                elif "closing notepad" in reply:
                    NonInputExecution(reply)
                    
                elif "opening gmail" in reply:
                    NonInputExecution(reply)
                    
                elif "opening amazon" in reply:
                    NonInputExecution(reply)
                    
                elif "opening github" in reply:
                    NonInputExecution(reply)
                    
                elif "cmd" in reply:
                    NonInputExecution(reply)
                    
                elif "open telegram" in reply:
                    NonInputExecution(reply)
                    
                elif "opening chrome" in reply:
                    NonInputExecution(reply)
                    
                elif "closing chrome" in reply:
                    NonInputExecution(reply)
                    
                elif "opening gmail" in reply:
                    NonInputExecution(reply)
                    
                elif "opening amazon" in reply:
                    NonInputExecution(reply)
                    
                elif "opening flipkart" in reply:
                    NonInputExecution(reply)
                    
                elif "faded" in reply:
                    NonInputExecution(reply)
                    
                elif "worlds collide" in reply:
                    NonInputExecution(reply)
                    
                elif "Alarm" in reply:
                    NonInputExecution(reply)
                    
                elif "TimeTable" in reply:
                    NonInputExecution(reply)
                    
                elif "Temperature" in reply:
                    NonInputExecution(reply)

                elif "Weather" in reply:
                    NonInputExecution(reply)
                    
                elif "game" in reply:
                    NonInputExecution(reply)
                    
                elif "CA NT" in reply:
                    NonInputExecution(reply)
                    
                elif "CA CT" in reply:
                    NonInputExecution(reply)
                    
                elif "CA NW" in reply:
                    NonInputExecution(reply)
                    
                elif "CA H" in reply:
                    NonInputExecution(reply)
                    
                elif "CA D" in reply:
                    NonInputExecution(reply)
                    
                elif "CA B" in reply:
                    NonInputExecution(reply)
                    
                elif "CA I" in reply:
                    NonInputExecution(reply)
                    
                elif "CA ST" in reply:
                    NonInputExecution(reply)
                    
                elif "YT P" in reply:
                    NonInputExecution(reply)
                    
                elif "YT R" in reply:
                    NonInputExecution(reply)
                    
                elif "YT FS" in reply:
                    NonInputExecution(reply)
                    
                elif "YT FM" in reply:
                    NonInputExecution(reply)
                    
                elif "YT S" in reply:
                    NonInputExecution(reply)
                    
                elif "YT B" in reply:
                    NonInputExecution(reply)
                    
                elif "YT I" in reply:
                    NonInputExecution(reply)
                    
                elif "YT D" in reply:
                    NonInputExecution(reply)
                    
                elif "YT PV" in reply:
                    NonInputExecution(reply)
                    
                elif "YT N" in reply:
                    NonInputExecution(reply)
                    
                elif "YT M" in reply:
                    NonInputExecution(reply)
                    
                elif "YT U" in reply:
                    NonInputExecution(reply)
                
                elif "YT MC" in reply:
                    NonInputExecution(reply)
                    
                elif "WA HS" in reply:
                    NonInputExecution(reply)
                    
                elif "WA M" in reply:
                    NonInputExecution(reply)
                    
                elif "WA STRT" in reply:
                    NonInputExecution(reply)
                    
                elif "WA STNGS" in reply:
                    NonInputExecution(reply)
                    
                elif "WA SRH" in reply:
                    NonInputExecution(reply)
                    
                elif "WA Screenshot" in reply:
                    NonInputExecution(reply)
                    
                elif "WA RW" in reply:
                    NonInputExecution(reply)
                    
                elif "remember that" in reply:
                    NonInputExecution(reply)
                    
                elif "BatteryL" in reply:
                    NonInputExecution(reply)
                    
                elif "Memory" in reply:
                    NonInputExecution(reply)
                    
                elif "CPUL" in reply:
                    NonInputExecution(reply)
                    
                elif "SystemStats" in reply:
                    NonInputExecution(reply)
                    
                elif "you dont said to remember" in reply:
                    NonInputExecution(reply)
                    
                else:
                    Say(reply)
                    
