import tkinter as tk
import os
from tkinter import Tk, Label, Button, Entry, END
from PIL import Image, ImageTk  
import tkinter.messagebox as messagebox
import random

# main loop starts here
SaveMe = Tk()
SaveMe.geometry("1000x1000")
SaveMe["background"] = "#1C1C1E"
SaveMe.title("SaveMe")
SaveMe.resizable(width=0, height=0)
basedir = os.path.dirname(os.path.abspath(__file__))

# Load and resize images
def load_image(image_name):
    image_path = os.path.join(basedir, "assets", image_name)
    image = Image.open(image_path)
    image = image.resize((1000, 1000), Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(image)

# Load images
sImage = load_image("sroom.png")
hauntedImage = load_image("hauntedmansion.png")
room1Image = load_image("room1.png")
room2Image = load_image("room2.png")
room3Image = load_image("room3.png")
room4Image = load_image("room4.png")
room5Image = load_image("room5.png")
finalImage = load_image("final.png")

# Font settings
FONT_MAIN = ("Helvetica", 16)
FONT_TITLE = ("Helvetica", 20, "bold")
FONT_SUBTITLE = ("Helvetica", 14)

#___________________MAIN_______________________________
def startscreen():
    # Set the background image
    sLabel = Label(SaveMe, image=sImage, background="#1C1C1E")
    sLabel.place(x=0, y=0, relwidth=1, relheight=1)  
    
    # Create a "BEGIN!" button in the center of the screen
    sbutton = Button(SaveMe, text="BEGIN!", borderwidth=0, highlightthickness=0, command=firstscreen, 
                     bg="#1C1C1E", fg="white", width=25, height=4, font=FONT_TITLE)
    sbutton.place(relx=0.5, rely=0.5, anchor='center')

def firstscreen():
    # Clear the current screen
    for widget in SaveMe.winfo_children():
        widget.destroy()

    # Function for "Yes" button
    def yes():    
        yesbutton.destroy()
        nobutton.destroy()
        letter.config(text="""The letter reads as follows:
                             \"Aaron, if you are reading this, you've taken the first step on a journey I've long envisioned. 
                             Hidden within those walls are truths waiting to be uncovered, and the key lies in your ability 
                             to decipher the clues....\"""",
                             font=("Helvetica", 14), fg="white", bg="#1C1C1E", wraplength=800)  
        conbutton.place(relx=0.5, rely=0.7, anchor='center')

    # Function for "No" button
    def no():
        SaveMe.quit()

    # Set the background image for the first screen
    sLabel = Label(SaveMe, image=sImage, background="#1C1C1E")
    sLabel.place(x=0, y=0, relwidth=1, relheight=1) 

    # Display the initial letter message
    letter = Label(SaveMe, text="""      *You are Aaron* 
                   You have received a letter. Click yes to continue.""", 
                   font=("Helvetica", 18), fg="white", bg="#1C1C1E", wraplength=800)  
    letter.place(relx=0.5, rely=0.4, anchor='center')  

    # Create "Yes" and "No" buttons for decision-making
    yesbutton = Button(SaveMe, text="Yes", borderwidth=0, highlightthickness=0, command=yes, 
                        bg="#1C1C1E", fg="white", width=10, height=2, font=("Helvetica", 14))
    yesbutton.place(relx=0.4, rely=0.55, anchor='center')

    nobutton = Button(SaveMe, text="No", borderwidth=0, highlightthickness=0, command=no, 
                       bg="#1C1C1E", fg="white", width=10, height=2, font=("Helvetica", 14))
    nobutton.place(relx=0.6, rely=0.55, anchor='center')

    # "Continue" button for progressing after the letter is read
    conbutton = Button(SaveMe, text="Continue", borderwidth=0, highlightthickness=0, command=secondscreen,
                             bg="#1C1C1E", fg="white", width=10, height=2, font=("Helvetica", 14))



def secondscreen():
    # Clear the current screen
    for widget in SaveMe.winfo_children():
        widget.destroy()

    # Function to handle "Continue" button
    def proceed():
        conbutton.place_forget()
        quitbutton.place_forget()
        
        secondlabel.config(text="""*You decided to visit the mansion and unravel the mystery surrounding the letter by yourself.*
                                
                                Aaron: This place is very spooky, but I must find what awaits me here.
                                
                                *You see a guard walking towards you. You are scared but decide to talk to him.*
                                
                                Guard: You must be Aaron. Well, we were waiting for you.
                                Guard: This place houses secrets, and you must find them if you want to own it all.
                                
                                Aaron: What do you mean by that?
                                
                                Guard: You will find out. Five quests await you. Remember, you are not the only one.
                                
                                Aaron: There... are... others?
                                
                                Guard: That's all I have to say. Good luck. What awaits on the other side is for you to discover.""",
                             font=("Helvetica", 16), fg="white", bg="#1C1C1E", wraplength=850)
        nextbutton.place(relx=0.5, rely=0.85, anchor='center')

    # Function for the next button
    def nextinsecond():
        nextbutton.place_forget()
        secondlabel.config(text="""*While exploring the mansion, you stumble upon a familiar-looking room.
                                 But before you realize it, the door shuts behind you, trapping you inside.
                                 You spot a message on the wall that reads:
                                 "Solve the riddle if you want to escape. This is your first quest." *""",
                             font=("Helvetica", 16), fg="white", bg="#1C1C1E", wraplength=850)
        nextbutton.config(command=thirdscreen)
        nextbutton.place(relx=0.5, rely=0.85, anchor='center')

    # Function to quit the game
    def quitt():
        SaveMe.quit()  

    # Set the background image
    secLabel = Label(SaveMe, image=hauntedImage, background="#1C1C1E")
    secLabel.place(x=0, y=0, relwidth=1, relheight=1)  

    # Display the initial text
    secondlabel = Label(SaveMe, text="*You don't know who the sender was. Do you still want to proceed with it?*", 
                        font=("Helvetica", 22), fg="white", bg="#1C1C1E", wraplength=850)
    secondlabel.place(relx=0.5, rely=0.3, anchor='center')

    # Create "Continue" and "Quit" buttons
    conbutton = Button(SaveMe, text="Continue", borderwidth=0, highlightthickness=0, command=proceed,
                       bg="#1C1C1E", fg="white", width=15, height=2, font=("Helvetica", 16))
    conbutton.place(relx=0.4, rely=0.55, anchor='center')

    quitbutton = Button(SaveMe, text="Quit", borderwidth=0, highlightthickness=0, command=quitt, 
                        bg="#1C1C1E", fg="white", width=15, height=2, font=("Helvetica", 16))
    quitbutton.place(relx=0.6, rely=0.55, anchor='center')

    # Hidden "Next" button to appear later
    nextbutton = Button(SaveMe, text="Next", borderwidth=0, highlightthickness=0, command=nextinsecond,
                        bg="#1C1C1E", fg="white", width=15, height=2, font=("Helvetica", 16))
    nextbutton.place_forget() 


def thirdscreen():
    # Clear current screen
    for widget in SaveMe.winfo_children():
        widget.destroy()

    # Set the background image
    thiLabel = Label(SaveMe, image=room4Image, background="#1C1C1E")
    thiLabel.place(x=0, y=0, relwidth=1, relheight=1)

    # Display riddle text
    thirdlabel = Label(SaveMe, text="""*You search around the room and come across a paper.*
                       The paper reads:
                       "Elsa has four daughters, and each of her daughters has a brother. 
                       How many children does Elsa have?" """, 
                       font=("Helvetica", 22), fg="white", bg="#1C1C1E", wraplength=850)
    thirdlabel.place(relx=0.5, rely=0.3, anchor='center')

    # Label for answer input
    nlabel = Label(SaveMe, text="Enter your answer here:", font=("Helvetica", 18), fg="white", bg="#1C1C1E")
    nlabel.place(relx=0.5, rely=0.45, anchor='center')

    # Entry widget for answer
    answer = tk.Entry(SaveMe, font=("Helvetica", 18), width=10)
    answer.place(relx=0.5, rely=0.5, anchor='center')

    # Function to check riddle answer
    def riddlesolver():
        userans = answer.get().strip().upper()

        if userans == "5" or userans == "FIVE":
            messagebox.showinfo("Correct!", "You've solved the riddle!")
            correct()  
        else:
            messagebox.showerror("Incorrect", "Incorrect answer. Try again!")
            giveup.place(relx=0.5, rely=0.7, anchor='center')

    # Function for correct answer
    def correct():
        for widget in SaveMe.winfo_children():
            widget.place_forget()

        correctlabel = Label(SaveMe, text="""You have successfully solved this riddle. The door will open for you now.
                       This journey awaits more such Quests. Can you solve them?""", 
                       font=("Helvetica", 22), fg="white", bg="#1C1C1E", wraplength=850)
        correctlabel.place(relx=0.5, rely=0.3, anchor='center')

        nextbutton = Button(SaveMe, text="Next", borderwidth=0, highlightthickness=0, command=fourthscreen,
                            bg="#1C1C1E", fg="white", width=12, height=2, font=("Helvetica", 18))
        nextbutton.place(relx=0.5, rely=0.7, anchor='center')

    # Function for incorrect answer
    def incorrect():
        for widget in SaveMe.winfo_children():
            widget.place_forget()

        incorrectlabel = Label(SaveMe, text="""You have failed to solve this riddle.
                       We will let you go this time, but better luck next time!""", 
                       font=("Helvetica", 22), fg="white", bg="#1C1C1E", wraplength=850)
        incorrectlabel.place(relx=0.5, rely=0.3, anchor='center')

        nextbutton = Button(SaveMe, text="Next", borderwidth=0, highlightthickness=0, command=fourthscreen,
                            bg="#1C1C1E", fg="white", width=12, height=2, font=("Helvetica", 18))
        nextbutton.place(relx=0.5, rely=0.7, anchor='center')

    # Submit and Give Up buttons
    submitbut = Button(SaveMe, text="Submit", borderwidth=0, highlightthickness=0, command=riddlesolver,
                       bg="#1C1C1E", fg="white", width=12, height=2, font=("Helvetica", 18))
    submitbut.place(relx=0.5, rely=0.6, anchor='center')

    giveup = Button(SaveMe, text="Give Up!", borderwidth=0, highlightthickness=0, command=incorrect,
                    bg="#1C1C1E", fg="white", width=12, height=2, font=("Helvetica", 18))
    giveup.place_forget()

def fourthscreen():
    # Clear the current screen
    for widget in SaveMe.winfo_children():
        widget.destroy()

    # Set the background image
    four = Label(SaveMe, image=room2Image, background="#1C1C1E")
    four.place(x=0, y=0, relwidth=1, relheight=1) 

    # Display introductory text
    fourthlabel = Label(SaveMe, text="""* You end in a completely different hallway and realise there is no escaping this.
                        You will need to solve each quest as it is and each awaits a quest here. 
                        You enter the next room and stumble across a mannequin with a label which goes 
                        'Ready for Rock, Paper, and Scissors?'* """, 
                        font=("Helvetica", 22), fg="white", bg="#1C1C1E", wraplength=850)
    fourthlabel.place(relx=0.5, rely=0.3, anchor='center')

    # Function to play rock-paper-scissors
    def play(choice):
        options = ["Rock", "Paper", "Scissors"]
        mannequin = random.choice(options)
        if mannequin == choice:
            messagebox.showinfo("DRAW!", "You and the mannequin made the same choice")
            try_Again()
        elif (choice == "Rock" and mannequin == "Scissors") or \
             (choice == "Scissors" and mannequin == "Paper") or \
             (choice == "Paper" and mannequin == "Rock"):
            messagebox.showinfo("WIN!", "Congrats! You WIN this round!")
            nexxt()
        else:
            messagebox.showwarning("Defeat!", "You lost this round. Better luck next time!")
            nexxt()

    # Function for playing rock-paper-scissors
    def rockpapsci():
        for widget in SaveMe.winfo_children():
            widget.place_forget()
        four.place(x=0, y=0, relwidth=1, relheight=1)

         # Rock, Paper, Scissors buttons with increased spacing
        rock = Button(SaveMe, text="Rock", borderwidth=0, highlightthickness=0, command=lambda: play("Rock"),
                  bg="#1C1C1E", fg="white", width=12, height=2, font=("Helvetica", 18))
        rock.place(relx=0.3, rely=0.6, anchor='center')  # Adjusted to the left

        paper = Button(SaveMe, text="Paper", borderwidth=0, highlightthickness=0, command=lambda: play("Paper"),
                   bg="#1C1C1E", fg="white", width=12, height=2, font=("Helvetica", 18))
        paper.place(relx=0.5, rely=0.6, anchor='center')  # Centered

        scissors = Button(SaveMe, text="Scissors", borderwidth=0, highlightthickness=0, command=lambda: play("Scissors"),
                      bg="#1C1C1E", fg="white", width=12, height=2, font=("Helvetica", 18))
        scissors.place(relx=0.7, rely=0.6, anchor='center')  # Adjusted to the right


    # Retry in case of a draw
    def try_Again():
        for widget in SaveMe.winfo_children():
            widget.place_forget()
        four.place(x=0, y=0, relwidth=1, relheight=1)
        
        ta = Label(SaveMe, text="It's a draw! Try again!", font=("Helvetica", 22), fg="white", bg="#1C1C1E")
        ta.place(relx=0.5, rely=0.4, anchor='center')

        rock = Button(SaveMe, text="Rock", borderwidth=0, highlightthickness=0, command=lambda: play("Rock"),
                      bg="#1C1C1E", fg="white", width=12, height=2, font=("Helvetica", 18))
        rock.place(relx=0.4, rely=0.6, anchor='center')

        paper = Button(SaveMe, text="Paper", borderwidth=0, highlightthickness=0, command=lambda: play("Paper"),
                       bg="#1C1C1E", fg="white", width=12, height=2, font=("Helvetica", 18))
        paper.place(relx=0.5, rely=0.6, anchor='center')

        scissors = Button(SaveMe, text="Scissors", borderwidth=0, highlightthickness=0, command=lambda: play("Scissors"),
                          bg="#1C1C1E", fg="white", width=12, height=2, font=("Helvetica", 18))
        scissors.place(relx=0.6, rely=0.6, anchor='center')

    # Function for proceeding to the next screen after a win or loss
    def nexxt():
        for widget in SaveMe.winfo_children():
            widget.place_forget()
        four.place(x=0, y=0, relwidth=1, relheight=1)

        nextlabel = Label(SaveMe, text="""Mannequin: You will now proceed towards the next room where another Quest awaits. 
                        You will come across a box. That's where your next quest lies.""", 
                        font=("Helvetica", 22), fg="white", bg="#1C1C1E", wraplength=850)
        nextlabel.place(relx=0.5, rely=0.3, anchor='center')

        nextbutton = Button(SaveMe, text="Next", borderwidth=0, highlightthickness=0, command=fifthscreen,
                            bg="#1C1C1E", fg="white", width=12, height=2, font=("Helvetica", 18))
        nextbutton.place(relx=0.5, rely=0.7, anchor='center')

    # Skip the rock-paper-scissors game
    def skipp():
        for widget in SaveMe.winfo_children():
            widget.place_forget()
        four.place(x=0, y=0, relwidth=1, relheight=1)

        skiplabel = Label(SaveMe, text="""You decided to skip this round. :( """, 
                          font=("Helvetica", 22), fg="white", bg="#1C1C1E", wraplength=850)
        skiplabel.place(relx=0.5, rely=0.4, anchor='center')

        nextbutton = Button(SaveMe, text="Next", borderwidth=0, highlightthickness=0, command=fifthscreen,
                            bg="#1C1C1E", fg="white", width=12, height=2, font=("Helvetica", 18))
        nextbutton.place(relx=0.5, rely=0.7, anchor='center')

    # Yes and No buttons to play or skip
    yesbutton = Button(SaveMe, text="Yes", borderwidth=0, highlightthickness=0, command=rockpapsci,
                       bg="#1C1C1E", fg="white", width=12, height=2, font=("Helvetica", 18))
    yesbutton.place(relx=0.4, rely=0.75, anchor='center')

    nobutton = Button(SaveMe, text="No", borderwidth=0, highlightthickness=0, command=skipp,
                      bg="#1C1C1E", fg="white", width=12, height=2, font=("Helvetica", 18))
    nobutton.place(relx=0.6, rely=0.75, anchor='center')

def fifthscreen():
    # quest 3: bulls and cows
    for widget in SaveMe.winfo_children():
        widget.destroy()
    fif = Label(SaveMe, image=room3Image, background="#1C1C1E", height=1000, width=1000)
    fif.place(x=0, y=0, relwidth=1, relheight=1)

    # Quest description
    fifthlabel = Label(SaveMe, text="""Are you ready to play a round of BULLS AND COWS? 
Guess the secret 4-digit code and open the box.""",
                       font=("Helvetica", 22, "bold"), fg="white", bg="#1C1C1E", wraplength=800, justify="center")
    fifthlabel.place(relx=0.5, rely=0.25, anchor="center")

    def generate_code():
        return ''.join(random.sample('0123456789', 4))

    guess = 0
    max_guess = 7
    guess_history = []
    code = generate_code()

    def bullcows():
        nonlocal guess, guess_history, code
        for widget in SaveMe.winfo_children():
            widget.place_forget()

        fif.place(x=0, y=0, relwidth=1, relheight=1)

        # Instruction for user input
        p = Label(SaveMe, text="Enter your guess for the 4-digit code:", font=("Helvetica", 20), fg="white", bg="#1C1C1E")
        p.place(relx=0.5, rely=0.3, anchor="center")

        # Input field for guess
        guessentry = Entry(SaveMe, font=("Helvetica", 22), width=10, justify="center")
        guessentry.place(relx=0.5, rely=0.4, anchor="center")

        # Submit button
        guessbutton = Button(SaveMe, text="Submit", borderwidth=0, highlightthickness=0,
                             command=lambda: checkguess(guessentry.get()), 
                             bg="#ff5c5c", fg="white", width=12, height=2, font=("Helvetica", 16, "bold"))
        guessbutton.place(relx=0.5, rely=0.5, anchor="center")

    def checkguess(guess_code):
        nonlocal guess, guess_history, code

        if len(guess_code) != 4 or not guess_code.isdigit():
            messagebox.showwarning("Invalid Input", "Enter a valid 4-digit code.")
            return

        guess += 1
        guess_history.append(guess_code)
        bulls, cows = calculate_bullscows(guess_code)

        if bulls == 4:
            messagebox.showinfo("Success!", f"Congratulations! You guessed the code {code} in {guess} attempts!")
            sixthscreen()
        elif guess >= max_guess:
            messagebox.showwarning("Game Over", f"You've used all {max_guess} attempts! The code was {code}.")
            sixthscreen()
        else:
            res = Label(SaveMe, text=f"Bulls: {bulls}, Cows: {cows}", font=("Helvetica", 20), fg="white", bg="#1C1C1E")
            res.place(relx=0.5, rely=0.6, anchor="center")
            giveup.place(relx=0.5, rely=0.75, anchor="center")

    def calculate_bullscows(guess_code):
        nonlocal code
        bulls = sum(1 for i in range(4) if guess_code[i] == code[i])
        cows = sum(1 for digit in guess_code if digit in code) - bulls
        return bulls, cows

    # Option to skip the game
    def skipp():
        for widget in SaveMe.winfo_children():
            widget.place_forget()
        fif.place(x=0, y=0, relwidth=1, relheight=1)
        skiplabel = Label(SaveMe, text="""You decided to skip this round.""", font=("Helvetica", 22, "bold"), fg="white", bg="#1C1C1E", wraplength=800)
        skiplabel.place(relx=0.5, rely=0.3, anchor="center")

        nextbutton = Button(SaveMe, text="Next", borderwidth=0, highlightthickness=0, command=sixthscreen,
                            bg="#ff5c5c", fg="white", width=12, height=2, font=("Helvetica", 16, "bold"))
        nextbutton.place(relx=0.5, rely=0.5, anchor="center")

    # Buttons for Yes and No options
    yesbutton = Button(SaveMe, text="Yes", borderwidth=0, highlightthickness=0, command=bullcows,
                       bg="#5cb85c", fg="white", width=12, height=2, font=("Helvetica", 16, "bold"))
    yesbutton.place(relx=0.4, rely=0.85, anchor="center")

    nobutton = Button(SaveMe, text="No", borderwidth=0, highlightthickness=0, command=skipp,
                      bg="#d9534f", fg="white", width=12, height=2, font=("Helvetica", 16, "bold"))
    nobutton.place(relx=0.6, rely=0.85, anchor="center")

    # Give Up button (initially hidden)
    giveup = Button(SaveMe, text="Give Up!", borderwidth=0, highlightthickness=0, command=skipp,
                    bg="#ff5c5c", fg="white", width=12, height=2, font=("Helvetica", 16, "bold"))
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

                     Voice: "Smart guess! Now Goodluck." """, 
                     font=("Helvetica", 18), fg="white", bg="#1C1C1E", wraplength=700, justify="left")
    sixlabel.place(x=100, y=100) 

    word_list = ["HACKNIGHT", "ACM", "MAAYA", "QUADRANGLE", "RIYAL", "PAIN", "HACKTOBERFEST", "BUNSAMOSA"]  
    secret_word = random.choice(word_list).upper()
    guessed = []
    incorrect = 0
    max_attempts = 6
    display = list("_" * len(secret_word))  

    def hangman():
        for widget in SaveMe.winfo_children():
            widget.place_forget()
        
        six.place(x=0, y=0, relwidth=1, relheight=1)

        displaylabel = Label(SaveMe, text=" ".join(display), font=("Helvetica", 36), fg="white", bg="#1C1C1E")
        displaylabel.place(x=300, y=250)

        guessdisplay = Label(SaveMe, text="Guessed Letters: ", font=("Helvetica", 20), fg="white", bg="#1C1C1E")
        guessdisplay.place(x=300, y=450)

        guesslabel = Label(SaveMe, text=f"Guesses Remaining: {max_attempts - incorrect}", font=("Helvetica", 20), fg="white", bg="#1C1C1E")
        guesslabel.place(x=300, y=500)

        def update():
            displaylabel.config(text=" ".join(display)) 
            if "_" not in display:  
                messagebox.showinfo("CONGRATS!", "You guessed the word. Now you can read the Letter!")
                finalscreen()

            if incorrect >= max_attempts:  
                messagebox.showwarning("OOPS!", f"You will never know the contents of the letter! The word was '{secret_word}'.")
                finalscreen()

            guessdisplay.config(text="Guessed Letters: " + ", ".join(guessed))
            guesslabel.config(text=f"Guesses Remaining: {max_attempts - incorrect}")

        def guess_letter():
            nonlocal incorrect
            letter = guessentry.get().upper()  
            guessentry.delete(0, END)  

            if len(letter) != 1 or not letter.isalpha():
                messagebox.showwarning("Invalid Input", "Please enter a single alphabet.")
                return

            if letter in guessed:
                messagebox.showwarning("Already Guessed", f"You have already guessed {letter}.")
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

        guessentry = Entry(SaveMe, font=("Helvetica", 20), width=5)
        guessentry.place(x=400, y=350)

        guessbutton = Button(SaveMe, text="Submit", borderwidth=0, highlightthickness=0, 
                              command=guess_letter, bg="#252526", fg="white", width=10, height=2, font=("Helvetica", 14))
        guessbutton.place(x=550, y=350)

    def skipp():
        for widget in SaveMe.winfo_children():
            widget.place_forget()
        six.place(x=0, y=0, relwidth=1, relheight=1)

        skiplabel = Label(SaveMe, text="""You decided to skip this round. :( """, font=("Helvetica", 20), fg="white", bg="#1C1C1E", wraplength=800)
        skiplabel.place(x=200, y=200)

        nextbutton = Button(SaveMe, text="Next", borderwidth=0, highlightthickness=0, command=finalscreen,
                            bg="#252526", fg="white", width=10, height=2, font=("Helvetica", 14))
        nextbutton.place(x=450, y=500)

    yesbutton = Button(SaveMe, text="Yes", borderwidth=0, highlightthickness=0, command=hangman, 
                        bg="#252526", fg="white", width=10, height=2, font=("Helvetica", 14), padx=10, pady=10)
    yesbutton.place(x=350, y=700) 

    nobutton = Button(SaveMe, text="No", borderwidth=0, highlightthickness=0, command=skipp, 
                       bg="#252526", fg="white", width=10, height=2, font=("Helvetica", 14), padx=10, pady=10)
    nobutton.place(x=500, y=700)

def finalscreen(quests_completed):
    # Clear the screen for the final ending screen
    for widget in SaveMe.winfo_children():
        widget.destroy() 
    
    # Background image for final screen
    fLabel = Label(SaveMe, image=finalImage, background="#1C1C1E", height=1000, width=1000)
    fLabel.place(x=0, y=0, relwidth=1, relheight=1) 

    # Define the different endings based on the number of completed quests
    if quests_completed < 2:
        ending_text = """BAD ENDING:
        You failed to complete most of the quests. The mystery remains unsolved, and the letter burns away. 
        Your journey ends here, and you will never know the truth..."""
    elif 2 <= quests_completed <= 3:
        ending_text = """OKAY ENDING:
        You completed some of the quests. The letter is partly readable, and you have learned some important information,
        but the mystery remains incomplete. Not bad, but there’s still more to uncover..."""
    else:
        ending_text = """GOOD ENDING:
        You completed all the quests successfully! The letter reveals its full content, and the mystery is solved. 
        You can leave the room with all the knowledge you've gained. Congratulations on your achievement!"""

    # Final label to display the ending message
    final_label = Label(SaveMe, text=ending_text, font=("Helvetica", 20), fg="white", bg="#1C1C1E", wraplength=800, justify="left")
    final_label.place(x=100, y=200)

    # Add a button to restart or exit the game
    exit_button = Button(SaveMe, text="Exit", borderwidth=0, highlightthickness=0, command=SaveMe.quit, 
                         bg="#252526", fg="white", width=10, height=2, font=("Helvetica", 14), padx=10, pady=10)
    exit_button.place(x=450, y=500)


startscreen()  
SaveMe.mainloop()
