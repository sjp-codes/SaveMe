import tkinter as tk
import os
from tkinter import Tk, Label, Button, Entry, END
from PIL import Image, ImageTk  
import tkinter.messagebox as messagebox
import random

# main loop starts here
SaveMe = Tk()
SaveMe.geometry("1000x1000")
SaveMe["background"]= "#1C1C1E"
SaveMe.title("SaveMe")
SaveMe.resizable(width=0, height=0)
basedir = os.getcwd()  
#____________________IMAGES_______________________
sImage = Image.open(os.path.join(basedir, "assets", "sroom.png"))
sImage = sImage.resize((1000, 1000), Image.Resampling.LANCZOS)  
sImage = ImageTk.PhotoImage(sImage)  

hauntedImage = Image.open(os.path.join(basedir, "assets", "hauntedmansion.png"))
hauntedImage = hauntedImage.resize((1000, 1000), Image.Resampling.LANCZOS)
hauntedImage = ImageTk.PhotoImage(hauntedImage)

room1Image = Image.open(os.path.join(basedir, "assets", "room1.png"))
room1Image = room1Image.resize((1000, 1000), Image.Resampling.LANCZOS)
room1Image = ImageTk.PhotoImage(room1Image)

room2Image = Image.open(os.path.join(basedir, "assets", "room2.png"))
room2Image = room2Image.resize((1000, 1000), Image.Resampling.LANCZOS)
room2Image = ImageTk.PhotoImage(room2Image)

room5Image = Image.open(os.path.join(basedir, "assets", "room5.png"))
room5Image = room5Image.resize((1000, 1000), Image.Resampling.LANCZOS)
room5Image = ImageTk.PhotoImage(room5Image)

room3Image = Image.open(os.path.join(basedir, "assets", "room3.png"))
room3Image = room3Image.resize((1000, 1000), Image.Resampling.LANCZOS)
room3Image = ImageTk.PhotoImage(room3Image)

room4Image = Image.open(os.path.join(basedir, "assets", "room4.png"))
room4Image = room4Image.resize((1000, 1000), Image.Resampling.LANCZOS)
room4Image = ImageTk.PhotoImage(room4Image)

finalImage = Image.open(os.path.join(basedir, "assets", "final.png"))
finalImage = finalImage.resize((1000, 1000), Image.Resampling.LANCZOS)
finalImage = ImageTk.PhotoImage(finalImage)

#___________________MAIN_______________________________
def startscreen():
    # start screen
    sLabel = Label(SaveMe, image=sImage, background="#1C1C1E", height=1000, width=1000)
    sLabel.place(x=0, y=0, relwidth=1, relheight=1)  
    
    sbutton = Button(SaveMe, text="BEGIN!", borderwidth=0, highlightthickness=0, command=firstscreen, 
                     bg="#1C1C1E", fg="white", width=25, height=4, font=("Helvetica", 18))
    sbutton.place(x=350, y=350)

def firstscreen():
    # the story begins
    for widget in SaveMe.winfo_children():
        widget.destroy()

    def yes():    
        yesbutton.destroy()
        nobutton.destroy()
        letter.config(text="""The letter reads as follows:
                            
                            \"Aaron, if you are reading this, you've taken the first step on a journey I've long envisioned. 
            Hidden within those walls are truths waiting to be uncovered, and the key lies in your ability to decipher the clues....\"""",
                             font=("Helvetica", 14), fg="white", bg="#1C1C1E", wraplength=800)  
        
        conbutton.place(x=400, y=500)

    def no():
        SaveMe.quit()

    sLabel = Label(SaveMe, image=sImage, background="#1C1C1E", height=1000, width=1000)
    sLabel.place(x=0, y=0, relwidth=1, relheight=1) 

    letter = Label(SaveMe, text="""      *You are Aaron*
                   You have received a letter. Click yes to continue.""", 
                         font=("Helvetica", 18), fg="white", bg="#1C1C1E", wraplength=800)  
    letter.place(x=100, y=300)  

    yesbutton = Button(SaveMe, text="Yes", borderwidth=0, highlightthickness=0, command=yes, 
                        bg="#1C1C1E", fg="white", width=10, height=2, font=("Helvetica", 14))
    yesbutton.place(x=350, y=400)

    nobutton = Button(SaveMe, text="No", borderwidth=0, highlightthickness=0, command=no, 
                       bg="#1C1C1E", fg="white", width=10, height=2, font=("Helvetica", 14))
    nobutton.place(x=500, y=400)

    conbutton = Button(SaveMe, text="Continue", borderwidth=0, highlightthickness=0, command=secondscreen,
                             bg="#1C1C1E", fg="white", width=10, height=2, font=("Helvetica", 14))

def secondscreen():
    # visiting the mansion and the initial quest is mentioned
    for widget in SaveMe.winfo_children():
        widget.destroy()

    def proceed():
        conbutton.place_forget()
        quitbutton.place_forget()
        
        secondlabel.config(text="""*You decided to visit the mansion and unravel the mystery surrounding the letter by yourself*
                         
                                Aaron: This place is very spooky but I must find what awaits me here.
                         
                                *You see a guard who walks towards you. You are scared but regardless decide to talk to him*
                         
                                Guard: You must be Aaron. Well, we were waiting for you.
                                Guard: This place houses secrets, and you must find them if you want to own it all by yourself.
                         
                                Aaron: What do you mean by that?
                         
                                Guard: You will find out for yourself. 5 quests await you. Remember, you are not the only one.
                         
                                Aaron: There...are...others?
                         
                                Guard: That is all I have to say to you. Good luck. What awaits on the other end is for you to find out.""",
                             font=("Helvetica", 14), fg="white", bg="#1C1C1E", wraplength=800)

        nextbutton.place(x=450, y=800)
    def nextinsecond():
        nextbutton.place_forget()
        secondlabel.config(text="""*While you were looking around the mansion, you stumble across a room which looks familiar. 
                         But before you know it, the door shuts on you and you're stuck there. 
                         You stumble across a message on the wall which reads:
                            "Solve the riddle if you want to see yourself out. This is your first quest." *""",
                         font=("Helvetica", 14), fg="white", bg="#1C1C1E", wraplength=800)
        nextbutton.config(command=thirdscreen)
        nextbutton.place(x=450, y=800)

            
    def quitt():
        SaveMe.quit()  
    secLabel = Label(SaveMe, image=hauntedImage, background="#1C1C1E", height=1000, width=1000)
    secLabel.place(x=0, y=0, relwidth=1, relheight=1)  

    secondlabel = Label(SaveMe, text="*You don't know who the sender was. Do you still want to proceed with it?*", font=("Helvetica", 20), fg="white", bg="#1C1C1E")
    secondlabel.place(x=100, y=200)

    conbutton = Button(SaveMe, text="Continue", borderwidth=0, highlightthickness=0, command=proceed,
                       bg="#1C1C1E", fg="white", width=10, height=2, font=("Helvetica", 14))
    conbutton.place(x=350, y=400)

    quitbutton = Button(SaveMe, text="Quit", borderwidth=0, highlightthickness=0, command=quitt, 
                        bg="#1C1C1E", fg="white", width=10, height=2, font=("Helvetica", 14))
    quitbutton.place(x=500, y=400)

    nextbutton = Button(SaveMe, text="Next", borderwidth=0, highlightthickness=0, command=nextinsecond,
                        bg="#1C1C1E", fg="white", width=10, height=2, font=("Helvetica", 14))
    nextbutton.place_forget() 


def thirdscreen():
    # quest 1 : solve the riddle
    for widget in SaveMe.winfo_children():
        widget.destroy()

    thiLabel = Label(SaveMe, image=room4Image, background="#1C1C1E", height=1000, width=1000)
    thiLabel.place(x=0, y=0, relwidth=1, relheight=1)  

    thirdlabel = Label(SaveMe, text="""*You search around the room and come across a paper*
                       The paper reads:
                       "Elsa has four daughters, and each of her daughters has a brother. 
                       How many children does Elsa have?" """, font=("Helvetica", 20), fg="white", bg="#1C1C1E", wraplength=800)
    thirdlabel.place(x=100, y=200)

    nlabel = Label(SaveMe, text="Enter your answer here:", font=("Helvetica", 14), fg="white", bg="#1C1C1E")
    nlabel.place(x=350, y=400)

    answer = tk.Entry(SaveMe, font=("Helvetica", 14), width=10)
    answer.place(x=350, y=450)

    def riddlesolver():
        userans = answer.get().strip().upper()

        if userans == "5" or userans == "FIVE":
            messagebox.showinfo("Correct!", "You've solved the riddle!")
            correct()  
        else:
            messagebox.showerror("Incorrect", "Incorrect answer. Try again!")
            giveup.place(x=500, y=500)  

    def correct():
        for widget in SaveMe.winfo_children():
            widget.place_forget()

        correctlabel = Label(SaveMe, text="""You have successfully solved this riddle. The door will open for you now.
                       This journey awaits more such Quests. Can you solve them?""", font=("Helvetica", 20), fg="white", bg="#1C1C1E", wraplength=800)
        correctlabel.place(x=100, y=200)

        nextbutton = Button(SaveMe, text="Next", borderwidth=0, highlightthickness=0, command=fourthscreen,
                            bg="#1C1C1E", fg="white", width=10, height=2, font=("Helvetica", 14))
        nextbutton.place(x=450, y=500)

    def incorrect():
        for widget in SaveMe.winfo_children():
            widget.place_forget()

        incorrectlabel = Label(SaveMe, text="""You have failed to solve this riddle.
                       We will let you go this time, but better luck next time!""", font=("Helvetica", 20), fg="white", bg="#1C1C1E", wraplength=800)
        incorrectlabel.place(x=100, y=200)

        nextbutton = Button(SaveMe, text="Next", borderwidth=0, highlightthickness=0, command=fourthscreen,
                            bg="#1C1C1E", fg="white", width=10, height=2, font=("Helvetica", 14))
        nextbutton.place(x=450, y=500)

    submitbut = Button(SaveMe, text="Submit", borderwidth=0, highlightthickness=0, command=riddlesolver,
                       bg="#1C1C1E", fg="white", width=10, height=2, font=("Helvetica", 14))
    submitbut.place(x=350, y=500)
    giveup = Button(SaveMe, text="Give Up!", borderwidth=0, highlightthickness=0, command=incorrect,
                    bg="#1C1C1E", fg="white", width=10, height=2, font=("Helvetica", 14))
    giveup.place_forget()  



def fourthscreen():
    # quest 2 : rock, paper and scissors
    for widget in SaveMe.winfo_children():
        widget.destroy()
    four = Label(SaveMe, image=room2Image, background="#1C1C1E", height=1000, width=1000)
    four.place(x=0, y=0, relwidth=1, relheight=1) 

    fourthlabel = Label(SaveMe, text="""* You end in a completely different hallway and realise there is no escaping this.
                            You will need to solve each quest as it is and each awaits a quest here. 
                        You enter the next room and stumble across a mannequin with a label which goes "Ready for Rock, Paper and Scissors?"* 
                        """, font=("Helvetica", 20), fg="white", bg="#1C1C1E", wraplength=800)
    fourthlabel.place(x=100, y=200)
    
    def play(choice):
        options = ["Rock", "Paper", "Scissors"]
        mannequin = random.choice(options)
        if mannequin == choice:
            messagebox.showinfo("DRAW!","You and the mannequin made the same choice")
            try_Again()
        elif (choice == "Rock" and mannequin == "Scissors") or \
                (choice == "Scissors" and mannequin == "Paper") or \
                (choice == "Paper" and mannequin == "Rock"):
            messagebox.showinfo("WIN!","Congrats! You WIN this round!")
            nexxt()
        else:
            messagebox.showwarning("Defeat!","You lost this round. Better luck next time!")
            nexxt()

    def rockpapsci():
        for widget in SaveMe.winfo_children():
            widget.place_forget()
        four.place(x=0, y=0, relwidth=1, relheight=1)

        # def play(choice):
        #     options = ["Rock", "Paper", "Scissors"]
        #     mannequin = random.choice(options)
        #     if mannequin == choice:
        #         messagebox.showinfo("DRAW!","You and the mannequin made the same choice")
        #         try_Again()
        #     elif (choice == "rock" and mannequin == "scissors") or \
        #         (choice == "scissors" and mannequin == "paper") or \
        #         (choice == "paper" and mannequin == "rock"):
        #         messagebox.showinfo("WIN!","Congrats! You WIN this round!")
        #     else:
        #         messagebox.showwarning("Defeat!","You lost this round. Better luck next time!")


        rock = Button(SaveMe, text="Rock", borderwidth=0, highlightthickness=0, command=lambda: play("Rock"), 
                       bg="#1C1C1E", fg="white", width=10, height=2, font=("Helvetica", 14)).place(x=300, y=400)
        paper = Button(SaveMe, text="Paper", borderwidth=0, highlightthickness=0, command=lambda: play("Paper"), 
                       bg="#1C1C1E", fg="white", width=10, height=2, font=("Helvetica", 14)).place(x=450, y=400)
        scissors = Button(SaveMe, text="Scissors", borderwidth=0, highlightthickness=0, command=lambda: play("Scissors"), 
                       bg="#1C1C1E", fg="white", width=10, height=2, font=("Helvetica", 14)).place(x=600, y=400)

        
    def try_Again():
        for widget in SaveMe.winfo_children():
            widget.place_forget()
        four.place(x=0, y=0, relwidth=1, relheight=1)
        ta = Label(SaveMe, text="It's a draw! Try again!", font=("Helvetica", 20), fg="white", bg="#1C1C1E")
        ta.place(x=350, y=300)
        rock = Button(SaveMe, text="Rock", borderwidth=0, highlightthickness=0, command=lambda: play("Rock"), 
                    bg="#1C1C1E", fg="white", width=10, height=2, font=("Helvetica", 14))
        rock.place(x=300, y=400)

        paper = Button(SaveMe, text="Paper", borderwidth=0, highlightthickness=0, command=lambda: play("Paper"), 
                    bg="#1C1C1E", fg="white", width=10, height=2, font=("Helvetica", 14))
        paper.place(x=450, y=400)

        scissors = Button(SaveMe, text="Scissors", borderwidth=0, highlightthickness=0, command=lambda: play("Scissors"), 
                        bg="#1C1C1E", fg="white", width=10, height=2, font=("Helvetica", 14))
        scissors.place(x=600, y=400)

    def nexxt():
        for widget in SaveMe.winfo_children():
            widget.place_forget()
        four.place(x=0, y=0, relwidth=1, relheight=1)
        fourthlabel = Label(SaveMe, text="""Mannequin: You will now proceed towards the next room where you await another Quest 
                        You will come across a box. That's where your next quest lies.""", font=("Helvetica", 20), fg="white", bg="#1C1C1E", wraplength=800)
        fourthlabel.place(x=100, y=200)
        nextbutton = Button(SaveMe, text="Next", borderwidth=0, highlightthickness=0, command=fifthscreen,
                            bg="#1C1C1E", fg="white", width=10, height=2, font=("Helvetica", 14))
        nextbutton.place(x=450, y=500)
        

    def skipp():
        for widget in SaveMe.winfo_children():
            widget.place_forget()
        four.place(x=0, y=0, relwidth=1, relheight=1)
        skiplabel = Label(SaveMe, text="""You decided to skip this round. :( """, font=("Helvetica", 20), fg="white", bg="#1C1C1E", wraplength=800)
        skiplabel.place(x=100, y=200)

        nextbutton = Button(SaveMe, text="Next", borderwidth=0, highlightthickness=0, command=fifthscreen,
                            bg="#1C1C1E", fg="white", width=10, height=2, font=("Helvetica", 14))
        nextbutton.place(x=450, y=500)
    
    yesbutton = Button(SaveMe, text="Yes", borderwidth=0, highlightthickness=0, command=rockpapsci, 
                        bg="#1C1C1E", fg="white", width=10, height=2, font=("Helvetica", 14))
    yesbutton.place(x=350, y=700) 

    nobutton = Button(SaveMe, text="No", borderwidth=0, highlightthickness=0, command=skipp, 
                       bg="#1C1C1E", fg="white", width=10, height=2, font=("Helvetica", 14))
    nobutton.place(x=500, y=700)

def fifthscreen():
    # quest 3 : bulls and cows
    for widget in SaveMe.winfo_children():
        widget.destroy()
    fif = Label(SaveMe, image=room3Image, background="#1C1C1E", height=1000, width=1000)
    fif.place(x=0, y=0, relwidth=1, relheight=1)

    fifthlabel = Label(SaveMe, text=""" Are you ready to play a round of BULLS AND COWS? 
                       Guess the secret 4 digit code and open the box""",
                        font=("Helvetica", 20), fg="white", bg="#1C1C1E")
    fifthlabel.place(x=100, y=200) 

    def generate_code():
        return ''.join(random.sample('0123456789', 4))
    guess = 0
    max_guess = 7
    guess_history = []
    code = generate_code()

    
    # code = ''.join(random.sample('0123456789', 4))

    def bullcows():
        nonlocal guess, guess_history, code
        print(code)  

        for widget in SaveMe.winfo_children():
            widget.place_forget()

        fif.place(x=0, y=0, relwidth=1, relheight=1)

        p = Label(SaveMe, text="Guess the 4-digit code:", font=("Helvetica", 20), fg="white", bg="#1C1C1E")
        p.place(x=100, y=200)

        guessentry = Entry(SaveMe, font=("Helvetica", 20), width=10)
        guessentry.place(x=350, y=300)

        guessbutton = Button(SaveMe, text="Submit", borderwidth=0, highlightthickness=0,
                             command=lambda: checkguess(guessentry.get()), 
                             bg="#1C1C1E", fg="white", width=10, height=2, font=("Helvetica", 14))
        guessbutton.place(x=350, y=400)

    def checkguess(guess_code):
        nonlocal guess, guess_history, code

        if len(guess_code) != 4 or not guess_code.isdigit():
            messagebox.showwarning("Invalid", "Enter a valid 4-digit code.")
            return

        guess += 1
        guess_history.append(guess_code)
        bulls, cows = calculate_bullscows(guess_code)

        # res = Label(SaveMe, text=f"Bulls: {bulls}, Cows: {cows}", font=("Helvetica", 20), fg="white", bg="#1C1C1E")
        # res.place(x=350, y=450)

        if bulls == 4:
            messagebox.showinfo("GUESSED IT!", f"You guessed the code {code} in {guess} attempts!")
            sixthscreen()
        elif guess >= max_guess:
            messagebox.showwarning("Better Luck :(", f"You've used all your {max_guess} attempts! The code was {code}.")
            sixthscreen()
        else:
            # res.config(text=f"Bulls: {bulls} , Cows: {cows}")
            res = Label(SaveMe, text=f"Bulls: {bulls}, Cows: {cows}", font=("Helvetica", 20), fg="white", bg="#1C1C1E")
            res.place(x=350, y=450)
            giveup.place(x=400,y=800)

    def calculate_bullscows(guess_code):
        nonlocal code
        bulls = sum(1 for i in range(4) if guess_code[i] == code[i])
        cows = sum(1 for digit in guess_code if digit in code) - bulls
        return bulls, cows

    def skipp():
        for widget in SaveMe.winfo_children():
            widget.place_forget()
        fif.place(x=0, y=0, relwidth=1, relheight=1)
        skiplabel = Label(SaveMe, text="""You decided to skip this round. :( """, font=("Helvetica", 20), fg="white", bg="#1C1C1E", wraplength=800)
        skiplabel.place(x=100, y=200)

        nextbutton = Button(SaveMe, text="Next", borderwidth=0, highlightthickness=0, command=sixthscreen,
                            bg="#1C1C1E", fg="white", width=10, height=2, font=("Helvetica", 14))
        nextbutton.place(x=450, y=500)

    yesbutton = Button(SaveMe, text="Yes", borderwidth=0, highlightthickness=0, command=bullcows, 
                        bg="#1C1C1E", fg="white", width=10, height=2, font=("Helvetica", 14))
    yesbutton.place(x=350, y=700) 

    nobutton = Button(SaveMe, text="No", borderwidth=0, highlightthickness=0, command=skipp, 
                       bg="#1C1C1E", fg="white", width=10, height=2, font=("Helvetica", 14))
    nobutton.place(x=500, y=700)
    giveup = Button(SaveMe, text="Give Up!", borderwidth=0, highlightthickness=0, command=skipp,
                    bg="#1C1C1E", fg="white", width=10, height=2, font=("Helvetica", 14))
    giveup.place_forget()  


def sixthscreen():
    # quest 4 : hangman
    for widget in SaveMe.winfo_children():
        widget.destroy()
    six = Label(SaveMe, image=room1Image, background="#1C1C1E", height=1000, width=1000)
    six.place(x=0, y=0, relwidth=1, relheight=1)

    sixlabel = Label(SaveMe, text="""*You find a key inside the box and figure out it unlocks a door in this room.
                     You open the door and you find a letter hanging from the ceiling near a candle. You hear a voice*
                     
                     Voice:"So you have made it until here. Congrats."
                     
                     Voice:"Your next QUEST is to guess the word. 
                     If you fail to guess it, the letter will burn before you get to read the contents "
                     
                     Aaron: "Is it sort of a HANGMAN game."

                     Voice: "Smart guess! Now Goodluck." """, font=("Helvetica", 20), fg="white", bg="#1C1C1E", wraplength=800)
    sixlabel.place(x=100, y=200) 

    word_list = ["HACKNIGHT" , "ACM" , "MAAYA" , "QUADRANGLE" , "RIYAL" ]  
    secret_word = random.choice(word_list)
    secret_word = secret_word.upper()
    guessed = []
    incorrect = 0
    max = 6
    display = list("_" * len(secret_word))  

    def hangman():
        print(secret_word)

        for widget in SaveMe.winfo_children():
            widget.place_forget()
        six.place(x=0, y=0, relwidth=1, relheight=1)

        displaylabel = Label(SaveMe, text=" ".join(display), font=("Helvetica", 40), fg="white", bg="#1C1C1E")
        displaylabel.place(x=350, y=300)

        guessdisplay = Label(SaveMe, text="Guessed Letters: ", font=("Helvetica", 20), fg="white", bg="#1C1C1E")
        guessdisplay.place(x=350, y=500)

        guesslabel = Label(SaveMe, text=f"Guess Remaining: {max - incorrect}", font=("Helvetica", 20), fg="white", bg="#1C1C1E")
        guesslabel.place(x=350, y=550)

        def update():
            displaylabel.config(text=" ".join(display)) 
            if "_" not in display:  
                messagebox.showinfo("CONGRATS!", "You guessed the word. Now you can read the Letter!")
                finalscreen()

            if incorrect >= max:  
                messagebox.showwarning("OOPS!", f"You will never know the contents of the letter! The word was '{secret_word}'.")
                finalscreen()

            guessdisplay.config(text="Guessed Letters: " + ", ".join(guessed))
            guesslabel.config(text=f"Guess Remaining: {max - incorrect}")

        def guess_letter():
            nonlocal incorrect
            try:
                letter = guessentry.get().upper()  
                guessentry.delete(0, END)  

                if len(letter) != 1 or not letter.isalpha():
                    messagebox.showwarning("Invalid", "Enter a single alphabet.")
                    return

                if letter in guessed:
                    messagebox.showwarning("Guessed Before", f"You have guessed {letter} before.")
                    return
                
                guessed.append(letter)  

                if letter in secret_word:
                    for i, char in enumerate(secret_word):
                        if char == letter:
                            display[i] = letter 
                    update()  
                else:
                    incorrect += 1 
                    update()  
            except Exception:
                print( f"An error occurred while processing your guess")

        guessentry = Entry(SaveMe, font=("Helvetica", 20), width=5)
        guessentry.place(x=350, y=400)

        guessbutton = Button(SaveMe, text="Submit", borderwidth=0, highlightthickness=0, 
                              command=guess_letter, bg="#1C1C1E", fg="white", width=10, height=2, font=("Helvetica", 14))
        guessbutton.place(x=350, y=450)

    def skipp():
        for widget in SaveMe.winfo_children():
            widget.place_forget()
        six.place(x=0, y=0, relwidth=1, relheight=1)
        skiplabel = Label(SaveMe, text="""You decided to skip this round. :( """, font=("Helvetica", 20), fg="white", bg="#1C1C1E", wraplength=800)
        skiplabel.place(x=100, y=200)

        nextbutton = Button(SaveMe, text="Next", borderwidth=0, highlightthickness=0, command=finalscreen,
                            bg="#1C1C1E", fg="white", width=10, height=2, font=("Helvetica", 14))
        nextbutton.place(x=450, y=500)

    yesbutton = Button(SaveMe, text="Yes", borderwidth=0, highlightthickness=0, command=hangman, 
                        bg="#1C1C1E", fg="white", width=10, height=2, font=("Helvetica", 14))
    yesbutton.place(x=350, y=700) 
    nobutton = Button(SaveMe, text="No", borderwidth=0, highlightthickness=0, command=skipp, 
                       bg="#1C1C1E", fg="white", width=10, height=2, font=("Helvetica", 14))
    nobutton.place(x=500, y=700)

## Add the seventh scene here!


def finalscreen():
    # the ending which depends on the number of quests completed.. <2: bad ending , 2-3 : okay ending, >3: good ending
    for widget in SaveMe.winfo_children():
        widget.destroy() 
    fLabel = Label(SaveMe, image=finalImage, background="#1C1C1E", height=1000, width=1000)
    fLabel.place(x=0, y=0, relwidth=1, relheight=1) 

    final = Label(SaveMe, text="""THE FINAL SCREEN. YOUR ENDING IS DECIDED HERE. """, font=("Helvetica", 20), fg="white", bg="#1C1C1E")
    final.place(x=100, y=200)


startscreen()  
SaveMe.mainloop()
