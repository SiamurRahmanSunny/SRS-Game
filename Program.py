# Importing Required Libraries
import tkinter as tk
from tkinter import messagebox
import random
# Importing Required Libraries

# Root Window
root = tk.Tk()
root.title("Game")
root.geometry("600x600")
root.configure(bg="orange")
root.resizable(False, False)
# Root Window

# Global Name Variable
user_name = tk.StringVar()
# Global Name Variable


# TIC TAC TOE

# TIC TAC TOE VARIABLES
buttons = [[None for _ in range(3)]for _ in range(3)]

player_turn = "X"
# TIC TAC TOE VARIABLES

def winner_check(): # This is for checking winner
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != " ":
            return True
    for col in range(3):
        if buttons[0][col]["text"] == buttons[1][col]["text"] == buttons[2][col]["text"] != " ":
            return True
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != " ":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != " ":
        return True
    return False

def tie_check(): # This is for checking tie
    for row in buttons:
        for button in row:
            if button["text"] == " ":
                return False
    return True

def reset_board(): # This is for reset the board
    global player_turn

    player_turn = "X"

    for row in buttons:
        for button in row:
            button.config(text=" ", state=tk.NORMAL)

def click(row, col): # This is for detecting click
    global player_turn

    buttons[row][col].config(text=player_turn, state=tk.DISABLED)

    if winner_check():
        messagebox.showinfo("Game-Over", f" Player {player_turn} Becomes Genius Win The Game How!")
        reset_board()
    elif tie_check():
        messagebox.showinfo("Game-Over", "LOL No One Is Genius Match Tie")
        reset_board()
    else:
        player_turn = "O" if player_turn == "X" else "X"

def board(): # This is for displaying Tic Tac Toe Board
    Design_instance.b1.config(text="Play Another Game", state=tk.NORMAL, command=select_game)

    for row in range(3):
        for col in range(3):
            button = tk.Button(Design_instance.f5, text=" ", bg="hot pink", fg="black", disabledforeground="black", font=("arial", 16), width="15", height="7", command=lambda r=row, c=col: click(r,c))
            button.grid(row=row, column=col)
            buttons[row][col] = button

# TIC TAC TOE


# IQ TEST

# IQ TEST VARIABLES
questions = ["What is 7+7?", "What is 8-4?", "What is 6*6?",
             "What is 8/2?", "What is 5+5?", "What is 9-3?",
             "What is 7*9?", "What is 8/4?", "What is 6+6?",
             "What is 9-1?"]

options = [["14", "16", "18", "20"], ["3", "4", "5", "6"], ["36", "42", "48", "54"],
           ["2", "3", "4", "5"], ["10", "12", "14", "16"], ["4", "5", "6", "7"],
           ["56", "63", "70", "77"], ["1", "2", "3", "4"], ["12", "14", "16", "18"],
           ["7", "11", "9", "8"]]

answers = [0, 1, 0, 2, 0, 2, 1, 1, 0, 3]

q_index = 0

score = 0

question_index = tk.IntVar()

selected_question = []
# IQ TEST VARIABLES

def check_answer(option): # This is for checking answer
    global q_index, score

    if option == answers[selected_question[q_index]]:
        score += 1
        Design_instance.b1.config(text="CORRECT!", state=tk.DISABLED)
    else:
        Design_instance.b1.config(text="WRONG!", state=tk.DISABLED)
    q_index += 1
    show_questions()

def show_questions(): # This is for displaying questions
    global selected_question, questions, options, answers, score, q_index

    selected_question = random.sample(range(len(questions)), question_index.get())

    if q_index < question_index.get():
        Design_instance.reset_f5()
        Design_instance.l1.config(text=f"{q_index + 1}. {questions[selected_question[q_index]]}")
        for i, option in enumerate(options[selected_question[q_index]]):
            option_button = tk.Button(
                Design_instance.f5,
                text=option,
                font=("Arial", 16),
                borderwidth=0,
                bg="blue",
                command=lambda o=i: check_answer(o)
            )
            option_button.pack(pady=10)
    else:
        Design_instance.reset_f5()
        Design_instance.l1.config(text=f"Your Score: {score}/{question_index.get()}")
        Design_instance.b1.config(text="Play Another Game", state=tk.NORMAL, command=select_game)

def submit_index(): # This is for submitting question index
    if question_index.get() < 3 or question_index.get() > 8:
        messagebox.showerror("Error", "Enter Question Between 3 to 8")
    else:
        messagebox.showinfo("Success", "Question Index Successfully Submitted")
        Design_instance.reset_f5()
        Design_instance.b1.config(text="Start The IQ Test", state=tk.NORMAL, command=show_questions)
        Design_instance.l1.config(text=f"Welcome {user_name.get()} to IQ Test. You Will Face {question_index.get()} Questions")

def start_iq(): # This is for starting IQ Test
    Design_instance.qindex_widget()
    Design_instance.b1.config(text="Submit Index", command=submit_index)
# IQ TEST


# HAND CRICKET

# HAND CRICKET VARIABLES
user_score = 0

ai_score = 0

user_wicket = 0

ai_wicket = 0

target = 0

ball = 0

user_ball = tk.IntVar()

toss_list = ["HEAD", "TAIL"]
# HAND CRICKET VARIABLES

def hc_reset(): # This is for reset the Hand Cricket Game
    global user_wicket, user_score, ball, target, ai_score, ai_wicket

    user_score = 0

    ai_score = 0

    user_wicket = 0

    ai_wicket = 0

    ball = 0

    target = 0

    Design_instance.reset_f5()

    Design_instance.b1.config(text="Play Another Game", state=tk.NORMAL, command=select_game)

def hc_bat_click(h): # This is for batting Logic
    global ai_choosed, user_wicket, user_score, ball, target, ai_score, ai_wicket

    if target == 0:
        ai_choosed = random.choice(["1", "2", "3", "4", "5", "6"])
        if h == ai_choosed:
            user_wicket += 1
        else:
            user_score += int(h)
        ball += 1
        Design_instance.reset_f5()
        Design_instance.b1.config(text=f"AI Choosed {ai_choosed}", state=tk.DISABLED)
        if ball == user_ball.get() or user_wicket == 10:
            target = user_score + 1
            Design_instance.reset_f5()
            ball = 0
            hc_bowl()
        else:
            return hc_bat()
    else:
        if user_score >= target:
            Design_instance.reset_f5()
            Design_instance.l1.config(text=f"{user_name.get()} Win The Match. Congrats! to You")
            return hc_reset()
        else:
            if ball == user_ball.get() or user_wicket == 10:
                if user_score >= target:
                    Design_instance.reset_f5()
                    Design_instance.l1.config(text=f"{user_name.get()} Win The Match. Congrats! to You")
                    return hc_reset()
                elif user_score == target:
                    Design_instance.reset_f5()
                    Design_instance.l1.config(text="Oh Wow! So Close. Match Draw")
                    return hc_reset()
                else:
                    Design_instance.reset_f5()
                    Design_instance.l1.config(text=f"{user_name.get()} Lost The Match. Congrats! to AI For Winning")
                    return hc_reset()
            else:
                ai_choosed = random.choice(["1", "2", "3", "4", "5", "6"])
                if h == ai_choosed:
                    user_wicket += 1
                else:
                    user_score += int(h)
                ball += 1
                Design_instance.reset_f5()
                Design_instance.b1.config(text=f"AI Choosed {ai_choosed}", state=tk.DISABLED)
                if user_score >= target:
                    Design_instance.reset_f5()
                    Design_instance.l1.config(text=f"{user_name.get()} Win The Match. Congrats! to You")
                    return hc_reset()
                return hc_bat()

def hc_bowl_click(hitballs): # This is for Bowling Logic
    global ai_choosed, user_wicket, user_score, ball, target, ai_score, ai_wicket

    if target == 0:
        ai_choosed = random.choice(["1", "2", "3", "4", "5", "6"])
        if hitballs == ai_choosed:
            ai_wicket += 1
        else:
            ai_score += int(ai_choosed)
        ball += 1
        Design_instance.reset_f5()
        Design_instance.b1.config(text=f"AI Choosed {ai_choosed}", state=tk.DISABLED)
        if ball == user_ball.get() or ai_wicket == 10:
            target = ai_score + 1
            Design_instance.reset_f5()
            ball = 0
            hc_bat()
        else:
            return hc_bowl()
    else:
        if ai_score >= target:
            Design_instance.reset_f5()
            Design_instance.l1.config(text=f"{user_name.get()} Win The Match. Congrats! to You")
            return hc_reset()
        else:
            if ball == user_ball.get() or user_wicket == 10:
                if ai_score >= target:
                    Design_instance.reset_f5()
                    Design_instance.l1.config(text=f"{user_name.get()} Lost The Match. Congrats! to AI For Winning")
                    return hc_reset()
                elif ai_score == target:
                    Design_instance.reset_f5()
                    Design_instance.l1.config(text="Oh Wow! So Close. Match Draw")
                    return hc_reset()
                else:
                    Design_instance.reset_f5()
                    Design_instance.l1.config(text=f"{user_name.get()} Win The Match. Congrats! to You")
                    return hc_reset()
            else:
                ai_choosed = random.choice(["1", "2", "3", "4", "5", "6"])
                if hitballs == ai_choosed:
                    ai_wicket += 1
                else:
                    ai_score += int(ai_choosed)
                ball += 1
                Design_instance.reset_f5()
                Design_instance.b1.config(text=f"AI Choosed {ai_choosed}", state=tk.DISABLED)
                if ai_score >= target:
                    Design_instance.reset_f5()
                    Design_instance.l1.config(text=f"{user_name.get()} Lost The Match. Congrats! to AI For Winning")
                    return hc_reset()
                return hc_bowl()

def hc_bat(): # This is for Batting
    global ai_choosed, user_wicket, user_score, ball, target, ai_score, ai_wicket

    Design_instance.reset_f5()

    Design_instance.l1.config(
        text=f"{user_name.get()} | Score: {user_score} ------> Wicket: {user_wicket} -----> Ball: {ball} ----> Target: {target}"
    )

    for i, hit in enumerate(["1", "2", "3", "4", "5", "6"]):
        hit_button = tk.Button(
            Design_instance.f5,
            text=hit,
            font=("Arial", 16),
            borderwidth=0,
            bg="blue",
            command=lambda h=hit: hc_bat_click(h)
        )
        hit_button.pack(pady=10)

def hc_bowl(): #This is for Bowling
    global ai_choosed, user_wicket, user_score, ball, target, ai_score, ai_wicket

    Design_instance.reset_f5()

    Design_instance.l1.config(text=f"AI | Score: {ai_score} ------> Wicket: {ai_wicket} -----> Ball: {ball} ----> Target: {target}")

    for i, hitball in enumerate(["1", "2", "3", "4", "5", "6"]):
        hitball_button = tk.Button(
            Design_instance.f5,
            text=hitball,
            font=("Arial", 16),
            borderwidth=0,
            bg="blue",
            command=lambda hitballs=hitball: hc_bowl_click(hitballs)
        )
        hitball_button.pack(pady=10)

def hc_batball_click(tb): # This is for choosing batting or bowling
    Design_instance.reset_f5()

    if tb == "BAT":
        hc_bat()
    else:
        hc_bowl()

def hc_toss_click(tc): # This is for Toss
    global ai_choose_toss, ai_choose_batball

    if tc == ai_choose_toss:
        Design_instance.reset_f5()
        Design_instance.l1.config(text=f"{user_name.get()} Won The Toss. Choose Batting or Bowling")
        for i, batballchoice in enumerate(["BAT", "BOWL"]):
            batball_button = tk.Button(
                Design_instance.f5,
                text=batballchoice,
                font=("Arial", 16),
                borderwidth=0,
                bg="blue",
                command=lambda tb=batballchoice: hc_batball_click(tb)
            )
            batball_button.pack(pady=10)
    else:
        Design_instance.reset_f5()
        ai_choose_batball = random.choice(["BAT", "BOWL"])
        Design_instance.l1.config(text=f"AI Won The Toss. AI Choose {ai_choose_batball}ING")
        if ai_choose_batball == "BAT":
            hc_bowl()
        else:
            hc_bat()
def hc_ball_click():
    global ai_choose_toss
    if user_ball.get() < 10 or user_ball.get() > 20:
        messagebox.showerror("Error", "Enter Ball Between 10 to 20")
    else:
        Design_instance.b1.config(text="", state=tk.DISABLED)
        ai_choose_toss = random.choice(toss_list)
        Design_instance.reset_f5()
        for i, toss in enumerate(toss_list):
            toss_button = tk.Button(
                Design_instance.f5,
                text=toss,
                font=("Arial", 16),
                borderwidth=0,
                bg="blue",
                command=lambda tc=toss: hc_toss_click(tc)
            )
            toss_button.pack(pady=10)
def hc_start():
    Design_instance.ball_widget()
    Design_instance.b1.config(text="Submit Ball", command=hc_ball_click)
# HAND CRICKET


# Guess The Number Game

# GUESS THE NUMBER VARIABLES
incorrect_gtn = 0
# GUESS THE NUMBER VARIABLES

def gtn_end(): # This is for ending the Guess The Number Game

    Design_instance.b1.config(text="Play Another Game", state=tk.NORMAL, command=select_game)

    Design_instance.reset_f5()

    Design_instance.l1.config(text="Match End! You Guessed The Number")
def gtn_click(): # This is for checking the number
    global incorrect_gtn, gtn_take, ai_gtn_take

    if gtn_take.get() == ai_gtn_take:
        messagebox.showinfo("Result", f"You Guessed The Correct Number. The Number Was {ai_gtn_take}")
        incorrect_gtn = 0
        gtn_end()
    else:
        if gtn_take.get() < ai_gtn_take:
            messagebox.showerror("Result", "Low")
        else:
            messagebox.showerror("Result", "High")
        incorrect_gtn += 1

        Design_instance.reset_f5()

        gtn_start()
def gtn_start(): # This is for starting the Guess The Number Game
    global incorrect_gtn, gtn_take, ai_gtn_take

    gtn_take = tk.IntVar()

    if incorrect_gtn < 11:
        Design_instance.b1.config(text="SUBMIT THE NUMBER", state=tk.NORMAL, command=gtn_click)
        Design_instance.l1.config(text="Incorrect " + str(incorrect_gtn))
        gtn_l1 = tk.Label(Design_instance.f5, text="Enter Number: ", font=("Arial", 16), bg="orange")
        gtn_l2 = tk.Entry(Design_instance.f5, textvariable=gtn_take, font=("Arial", 16), bg="grey")
        gtn_l1.pack(side="left")
        gtn_l2.pack(side="left")
    else:
        Design_instance.b1.config(text="Play Another Game", state=tk.NORMAL, command=select_game)

        Design_instance.reset_f5()

        Design_instance.l1.config(text="Match End! You Failed To Guess The Number")

        incorrect_gtn = 0
# Guess The Number Game


# Rock Paper Scissor Game

# Rock Paper Scissor Variables
rps_list = ["ROCK", "PAPER", "SCISSOR"]

round_rps = 1

rps_win = 0
# Rock Paper Scissor Variables

def rps_click(rc): # This is for Rock Paper Scissor Game Click
    global round_rps, ai_rps_choose, rps_win

    round_rps += 1

    ai_rps_choose = random.choice(rps_list)

    Design_instance.reset_f5()

    if rc == ai_rps_choose:
        messagebox.showinfo("Result", f"Match Draw. AI Choose {ai_rps_choose}")
    else:
        if rc == "ROCK" and ai_rps_choose == "SCISSOR" or \
                rc == "PAPER" and ai_rps_choose == "ROCK" or \
                rc == "SCISSOR" and ai_rps_choose == "PAPER":
            messagebox.showinfo("Result", f"{user_name.get()} Win. AI Choose {ai_rps_choose}")
            rps_win += 1
        else:
            messagebox.showinfo("Result", f"AI Win. AI Choose {ai_rps_choose}")
    Design_instance.b1.config(text="Next", state=tk.NORMAL, command=rps_start)

def rps_start(): # This is for starting the Rock Paper Scissor Game
    global round_rps

    if round_rps < 11:
        Design_instance.b1.config(text="", state=tk.DISABLED)

        Design_instance.l1.config(text="Round " + str(round_rps) + " Wins " + str(rps_win))

        for i,rps in enumerate(rps_list):
            rps_button = tk.Button(
                Design_instance.f5,
                text=rps,
                font=("Arial", 16),
                borderwidth=0,
                bg="blue",
                command=lambda rc=rps: rps_click(rc)
            )
            rps_button.pack(pady=10)
    else:
        Design_instance.b1.config(text="Play Another Game", state=tk.NORMAL, command=select_game)

        Design_instance.reset_f5()

        Design_instance.l1.config(text="Match End")

        round_rps = 0
# Rock Paper Scissor Game


# Function to select the game
def game_click(select):
    global selected_game, ai_gtn_take

    if select == "HAND CRICKET":
        Design_instance.reset_f5()

        Design_instance.l1.config(text="Welcome to Hand Cricket")

        Design_instance.b1.config(text="Start", state=tk.NORMAL, command=hc_start)
    elif select == "ROCK PAPER SCISSOR":
        Design_instance.reset_f5()

        Design_instance.l1.config(text="Welcome to Rock Paper Scissor")

        Design_instance.b1.config(text="Start", state=tk.NORMAL, command=rps_start)
    elif select == "TIC TAC TOE":
        Design_instance.reset_f5()

        Design_instance.l1.config(text="Welcome to Tic Tac Toe")

        Design_instance.b1.config(text="Start", state=tk.NORMAL, command=board)
    elif select == "GUESS THE NUMBER":
        Design_instance.reset_f5()

        Design_instance.l1.config(text="Welcome to Guess the Number")

        ai_gtn_take = random.randint(1, 100)

        Design_instance.b1.config(text="Start", state=tk.NORMAL, command=gtn_start)
    elif select == "IQ TEST":
        Design_instance.reset_f5()

        Design_instance.l1.config(text="Welcome to IQ Test")

        Design_instance.b1.config(text="Start", state=tk.NORMAL, command=start_iq)
    elif select == "CHANGE NAME":
        Design_instance.reset_f5()

        Design_instance.l1.config(text="Enter Your Name Again")

        Design_instance.name_again()

        Design_instance.b1.config(text="Submit", state=tk.NORMAL, command=select_game)
    else:
        messagebox.showerror("Error", "Invalid Game")
# Function to select the game
def select_game():
    global selected_game

    if user_name.get() == "":
        messagebox.showerror("Error", "Enter Your Name")
    else:
        Design_instance.b1.config(state=tk.NORMAL, text="EXIT", command=root.quit)

        Design_instance.reset_f5()

        Design_instance.l1.config(text="Welcome " + user_name.get())

        selected_game = random.choice(["HAND CRICKET", "ROCK PAPER SCISSOR", "TIC TAC TOE", "GUESS THE NUMBER", "IQ TEST", "CHANGE NAME"])

        for i,game in enumerate(["HAND CRICKET", "ROCK PAPER SCISSOR", "TIC TAC TOE", "GUESS THE NUMBER", "IQ TEST", "CHANGE NAME"]):
            game_button = tk.Button(
                Design_instance.f5,
                text=game,
                font=("Arial", 16),
                borderwidth=0,
                bg="blue",
                command=lambda gc=game: game_click(gc)
            )
            game_button.pack(pady=10)
# Main Design
class Design:
    def __init__(self, master):

        # FRAMES
        self.f1 = tk.Frame(master, bg="red")

        self.f2 = tk.Frame(master, bg="red")

        self.f3 = tk.Frame(master, bg="red")

        self.f4 = tk.Frame(master, bg="red")

        self.f5 = tk.Frame(master, bg="orange")
        # FRAMES

        # WIDGETS
        self.l1 = tk.Label(self.f1, text="Welcome to the Game", font=("Arial", 16), bg="red")

        self.l2 = tk.Label(self.f2, text="  ", font=("Arial", 16), bg="red")

        self.l3 = tk.Label(self.f3, text="  ", font=("Arial", 16), bg="red")

        self.b1 = tk.Button(self.f4, text="Submit", font=("Arial", 16), bg="red", borderwidth=0, command=select_game)

        self.l4 = tk.Label(self.f5, text="Enter Your Name: ", font=("Arial", 16), bg="orange")

        self.l5 = tk.Entry(self.f5, textvariable=user_name, font=("Arial", 16), bg="grey")
        # WIDGETS

        # PACKING FRAMES
        self.f1.pack(side="top", fill="x")

        self.f2.pack(side="left", fill="y")

        self.f3.pack(side="right", fill="y")

        self.f4.pack(side="bottom", fill="x")

        self.f5.pack(side="top", fill="x")
        # PACKING FRAMES

        # PACKING WIDGETS
        self.l1.pack()

        self.l2.pack()

        self.l3.pack()

        self.b1.pack(side="bottom", fill="x")

        self.l4.pack(side="left")

        self.l5.pack(side="left")
        # PACKING WIDGETS

    def reset_f5(self):
        for widget in Design_instance.f5.winfo_children():
            widget.destroy()

    def ball_widget(self):
        self.ball = tk.Label(self.f5, text="How Much Ball (10-20): ", font=("Arial", 16), bg="orange")

        self.ball_entry = tk.Entry(self.f5, textvariable=user_ball, font=("Arial", 16), bg="grey")

        self.ball.pack(side="left")

        self.ball_entry.pack(side="left")

    def name_again(self):
        self.name = tk.Entry(self.f5, textvariable=user_name, font=("Arial", 16), bg="grey")

        self.name.pack(side="left")

    def qindex_widget(self):
        self.qindex = tk.Label(self.f5, text="How Much Question You Want To Face (Choose Between 3-8): ", font=("Arial", 12), bg="orange")

        self.qindex_entry = tk.Entry(self.f5, textvariable=question_index, font=("Arial", 16), bg="grey")

        self.qindex.pack(side="left")

        self.qindex_entry.pack(side="left")

Design_instance = Design(root)


root.mainloop()