import pyttsx3  # pip install pyttsx3
import speech_recognition as sr
import random

def Say(Text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voices',voices[0].id)
    lengthcode = len(Text)

    if lengthcode>30:
        engine.setProperty('rate',200)

    else:
        engine.setProperty('rate',170)

    print("    ")
    print(f"Jarvis : {Text}")
    engine.say(text=Text)
    engine.runAndWait()
    print("    ")
    
def Listen() : 
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source,0,5)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"You : {query}\n")
    except Exception as e:
        print(e)
        return "None"
    return query

def RPS():
    Say("Lets Play Rock Paper Scissors!")
    Say("Choose")
    i = 0
    my_score = 0
    com_score = 0
    while (i<5):
        choose = ("rock","paper","scissors")
        com_choose = random.choice(choose)
        query = Listen()
        if (query == "rock"):
            if (com_choose == "rock"):
                Say("Rock!")
                Say("Draw!")
            elif (com_choose == "paper"):
                com_score += 1
                Say("paper!")
                Say("I Won!")
            elif (com_choose == "scissors"):
                my_score += 1
                Say("scissors!")
                Say("Ah! You won!")
            
        elif (query == "paper" ):
            if (com_choose == "rock"):
                my_score += 1
                Say("Rock!")
                Say("Ah! You won!")
            elif (com_choose == "paper"):
                Say("paper")
                Say("Draw!")
            elif (com_choose == "scissors"):
                com_score += 1
                Say("Paper!")
                Say("I Won!")
                
        elif (query == "scissor" & query == "scissors" ):
            if (com_choose == "rock"):
                com_score += 1
                Say("Paper!")
                Say("I Won!")
                
            elif (com_choose == "paper"):
                my_score += 1
                Say("Rock!")
                Say("Ah! You won!")
                
            elif (com_choose == "scissors"):
                Say("paper")
                Say("Draw!")
         else:
            Say("Say that again")
                
RPS()
