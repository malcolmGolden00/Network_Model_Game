import tkinter as tk
from tkinter import font
from random import randint, choice

from data_page import *
# 29/11/2020  Game written to practice learning about the main networking models.


root = tk.Tk()
root.minsize(height=1050, width=1920)
root.title("Practicing with Network Models")
screen_width = 700
screen_height = 700
# Fonts
title_font = font.Font(family="systemfixed", size=20)
title_caption_font = font.Font(family="systemfixed", size=12, slant="italic")
q_font = font.Font(family="systemfixed", size=20)
feedback_font = font.Font(family="systemfixed", size=12)
answer_format = font.Font(family="systemfixed", size=25)
entry_font = font.Font(family="systemfixed", size=25)
ans_chk_font = font.Font(family="systemfixed", size=15)
# Colors
white = "#ffffff"
grey = "#bdbdbd"
darker_grey = "#b0b0b0"
black = "#000000"
blue = "#4fc2ff"
green = "#4fff95"
yellow = "#f5ff4f"
red = "#ff4f4f"
purple = "#e4b3ff"
orange = "#f78224"

# Screen
main_screen = tk.Canvas(root, width=screen_width, height=screen_height, bg=grey)
main_screen.place(relx=0, rely=0, relheight=1, relwidth=1)
# title
title_label = tk.Label(main_screen, text="Practicing with Network Models", bg=grey, font=title_font)
title_label.place(relx=.05, rely=.005, relheight=.1, relwidth=.9)
# title caption
#title_caption = tk.Label(main_screen, text="Welcome and good luck. ????", bg=yellow, font=title_caption_font)
#title_caption.place(relx=.05, rely=.107, relheight=.1, relwidth=.9)

def start_game():
# debugger \ print(randint(1, 10))

# Unnecessary just placed the cur q container in its place.
#    info_screen_width = 0
#    info_screen_height = 0
#    info_screen = tk.Canvas(main_screen, width=info_screen_width, height=info_screen_height, bg=red)
#    info_screen.place(relx=.05, rely=.20833, relwidth=.9, relheight=.3)

# draw question block

    cur_q = choice(model_questions)
    q_index = model_questions.index(cur_q)
    print(q_index)
    cur_a_1 = answers[q_index][0]
    cur_a_2 = answers[q_index][1]
    cur_a_3 = answers[q_index][2]

    print(cur_a_1, cur_a_2, cur_a_3)
    #print(q_index, cur_a_1)
    #answer_2 = answers[q_index][1]
    #answer_3 = answers[q_index][2]

    #print(answer_1)
    #print(answer_2)
    #print(answer_3)

    q_text = tk.Label(main_screen, text=cur_q, bg=grey, fg=black, font=q_font)
    q_text.place(relx=.05, rely=.20833, relwidth=.9, relheight=.3)


#container for multilple widgets used in answer \ input block
    answer_screen_width = 0
    answer_screen_height = 0
    answer_screen = tk.Canvas(main_screen, width=answer_screen_width, height=answer_screen_height, bg=grey)
    answer_screen.place(relx=.05, rely=.55, relwidth=.9, relheight=.3)
# draw answer \ input block contents
    a_form_1 = tk.Label(answer_screen, text="This is layer number ", font=answer_format, bg=grey)
    a_form_1.place(relx=.005, rely=.1, relwidth=.25, relheight=.2)
    a_form_2 = tk.Label(answer_screen, text="of the ", font=answer_format, bg=grey)
    a_form_2.place(relx=.361, rely=.1, relwidth=.1, relheight=.2)
    a_form_3 = tk.Label(answer_screen, text="Model. The", font=answer_format, bg=grey)
    a_form_3.place(relx=.567, rely=.1, relwidth=.15, relheight=.2)
    a_form_4 = tk.Label(answer_screen, text="layer", font=answer_format, bg=grey)
    a_form_4.place(relx=.885, rely=.1, relwidth=.1, relheight=.2)
## Functions to place selections in entry boxes
    def set_num(text):
        entry_1.insert(0, text)
    def set_model(text):
        entry_2.insert(0, text)
    def set_layer(text):
        entry_3.insert(0, text)


    entry_1 = tk.Entry(answer_screen, font=entry_font)
    entry_1.place(relx=.258, rely=.1, relwidth=.1, relheight=.2)
    entry_2 = tk.Entry(answer_screen, font=entry_font)
    entry_2.place(relx=.463, rely=.1, relwidth=.1, relheight=.2)
    entry_3 = tk.Entry(answer_screen, font=entry_font)
    entry_3.place(relx=.7185, rely=.1, relwidth=.16, relheight=.2)
# Entry Buttons

    sel_num_1 = tk.Button(answer_screen, text="1", font=entry_font, command=lambda: set_num("1"))
    sel_num_1.place(relx=.025, rely=.6, relwidth=.025, relheight=.15)
    sel_num_2 = tk.Button(answer_screen, text="2", font=entry_font, command=lambda: set_num("2"))
    sel_num_2.place(relx=.05, rely=.6, relwidth=.025, relheight=.15)
    sel_num_3 = tk.Button(answer_screen, text="3", font=entry_font, command=lambda: set_num("3"))
    sel_num_3.place(relx=.075, rely=.6, relwidth=.025, relheight=.15)
    sel_num_4 = tk.Button(answer_screen, text="4", font=entry_font, command=lambda: set_num("4"))
    sel_num_4.place(relx=.1, rely=.6, relwidth=.025, relheight=.15)
    sel_num_5 = tk.Button(answer_screen, text="5", font=entry_font, command=lambda: set_num("5"))
    sel_num_5.place(relx=.125, rely=.6, relwidth=.025, relheight=.15)
    sel_num_6 = tk.Button(answer_screen, text="6", font=entry_font, command=lambda: set_num("6"))
    sel_num_6.place(relx=.15, rely=.6, relwidth=.025, relheight=.15)
    sel_num_7 = tk.Button(answer_screen, text="7", font=entry_font, command=lambda: set_num("7"))
    sel_num_7.place(relx=.175, rely=.6, relwidth=.025, relheight=.15)





    sel_model_1 = tk.Button(answer_screen, text="OSI", font=entry_font, command=lambda: set_model("OSI"))
    sel_model_1.place(relx=.4, rely=.6, relwidth=.1, relheight=.15)
    sel_model_2 = tk.Button(answer_screen, text="TCP / IP", font=entry_font, command=lambda: set_model("TCP / IP"))
    sel_model_2.place(relx=.5, rely=.6, relwidth=.1, relheight=.15)

    sel_layer_1 = tk.Button(answer_screen, text="Application", font=entry_font, comman=lambda: set_layer("Application"))
    sel_layer_1.place(relx=.8, rely=.80, relwidth=.15, relheight=.15)
    sel_layer_2 = tk.Button(answer_screen, text="Transport", font=entry_font, comman=lambda: set_layer("Transport"))
    sel_layer_2.place(relx=.8, rely=.65, relwidth=.15, relheight=.15)
    sel_layer_3 = tk.Button(answer_screen, text="Physical", font=entry_font, comman=lambda: set_layer("Physical"))
    sel_layer_3.place(relx=.8, rely=.50, relwidth=.15, relheight=.15)
    sel_layer_4 = tk.Button(answer_screen, text="Data Link", font=entry_font, comman=lambda: set_layer("Data Link"))
    sel_layer_4.place(relx=.8, rely=.35, relwidth=.15, relheight=.15)
    sel_layer_5 = tk.Button(answer_screen, text="Internet", font=entry_font, comman=lambda: set_layer("Internet"))
    sel_layer_5.place(relx=.65, rely=.80, relwidth=.15, relheight=.15)
    sel_layer_6 = tk.Button(answer_screen, text="Presentation", font=entry_font, comman=lambda: set_layer("Presentation"))
    sel_layer_6.place(relx=.65, rely=.65, relwidth=.15, relheight=.15)
    sel_layer_7 = tk.Button(answer_screen, text="Network", font=entry_font, comman=lambda: set_layer("Network"))
    sel_layer_7.place(relx=.65, rely=.50, relwidth=.15, relheight=.15)
    sel_layer_8 = tk.Button(answer_screen, text="Session", font=entry_font, comman=lambda: set_layer("Session"))
    sel_layer_8.place(relx=.65, rely=.35, relwidth=.15, relheight=.15)

# Function checking answers

    def ans_chk():
        if cur_a_1 == entry_1.get():
            correct = tk.Label(answer_screen, text="Correcrt", fg=green, font=ans_chk_font)
            correct.place(relx=.258, rely=.01, relwidth=.1, relheight=.07)
        else:
            incorrect = tk.Label(answer_screen, text="Incorrecrt", fg=red, font=ans_chk_font)
            incorrect.place(relx=.258, rely=.01, relwidth=.1, relheight=.07)
        if cur_a_2 == entry_2.get():
            correct = tk.Label(answer_screen, text="Correcrt", fg=green, font=ans_chk_font)
            correct.place(relx=.463, rely=.01, relwidth=.1, relheight=.07)
        else:
            incorrect = tk.Label(answer_screen, text="Incorrecrt", fg=red, font=ans_chk_font)
            incorrect.place(relx=.463, rely=.01, relwidth=.1, relheight=.07)
        if cur_a_3 == entry_3.get():
            correct = tk.Label(answer_screen, text="Correcrt", fg=green, font=ans_chk_font)
            correct.place(relx=.7185, rely=.01, relwidth=.1, relheight=.07)
        else:
            incorrect = tk.Label(answer_screen, text="Incorrecrt", fg=red, font=ans_chk_font)
            incorrect.place(relx=.75, rely=.01, relwidth=.1, relheight=.07)






    def help_window():
        help_root = tk.Tk()
        help_root.minsize(height=900, width=1000)
        help_root.title("Help Window")
    def exit_game():
        exit()

# Main Buttons
    help_button = tk.Button(main_screen, text="Need Help?", bg=darker_grey, command=help_window)
    help_button.place(relx=.005, rely=.01, relwidth=.07, relheight=.05)
    quit_button = tk.Button(main_screen, text="Quit", bg=darker_grey, command=exit_game)
    quit_button.place(relx=.025, rely=.9, relwidth=.1, relheight=.05)
    next_q_button = tk.Button(main_screen, text="Next", bg=darker_grey, command=start_game)
    next_q_button.place(relx=.875, rely=.9, relwidth=.1, relheight=.05)
    submit_button = tk.Button(main_screen, text="Submit", bg=darker_grey, command=ans_chk)
    submit_button.place(relx=.45, rely=.9, relwidth=.1, relheight=.05)

    #    input_screen =
    root.mainloop()

#initiate
start_game()
