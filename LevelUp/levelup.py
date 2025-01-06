import time
import tkinter as tk 
from threading import Thread
import pygame

pygame.mixer.init()

sounds ={
    1: pygame.mixer.Sound("alert/level1.wav"),
    2: pygame.mixer.Sound("alert/level2.wav"),
    3: pygame.mixer.Sound("alert/level3.wav"),
    4: pygame.mixer.Sound("alert/level4.wav"),
    5: pygame.mixer.Sound("alert/level5.wav"),
}

def update_mind_level(elapsed_time):
    if elapsed_time < 45*60:
        level = 1
        text = "Monkey Mind (level 1)"
    elif 45*60 <=elapsed_time < 90*60:
        level = 2
        text = "Beginner Mind (level 2)"
    elif 90*60 <=elapsed_time < 135*60:
        level = 3
        text = "Quiet Mind (level 3)"
    elif 135*60 <=elapsed_time < 180*60:
        level = 4
        text = "Awakened Mind (level 4)"
    else:
        level = 5
        text = "No Mind (level 5)"
    
    if mind_level.get() !=text:
        sounds[level].play()
    
    return text

def start_timer():
    global reset_flag
    reset_flag.set(False)
    elapsed_time = 0 
    while elapsed_time <= 180*60 and not reset_flag.get():
        time.sleep(1)
        elapsed_time +=1
        mind_level.set(update_mind_level(elapsed_time))
        hours = elapsed_time // 3600
        minutes = (elapsed_time % 3600) // 60
        seconds = elapsed_time % 60
        timer_label.config(text=f"Time Elapsed : {hours} hr {minutes} min {seconds} sec")
        root.update()

def reset_timer():
    global reset_flag
    reset_flag.set(True)
    timer_label.config(text="Time Elapsed: 0 hr 0 min 0 sec")
    mind_level.set("Empty mind (level 0)")

def run_timer():
    timer_thread = Thread(target=start_timer)
    timer_thread.daemon = True
    timer_thread.start()

root =tk.Tk()
root.title("Level Up")
root.configure(bg="#1C1C1C")

font_style = ("Terminal",12)
label_font = ("Terminal", 16,"bold")

mind_level = tk.StringVar()
mind_level.set("Empty Mind (level 0)")
reset_flag = tk.BooleanVar()

frame = tk.Frame(root, bg="#1C1C1C", bd=5, relief="solid", highlightbackground="green", highlightcolor="green", highlightthickness=2)
frame.pack(pady=20, padx=20, expand=True)

frame.rowconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)
frame.rowconfigure(2, weight=1)
frame.rowconfigure(3, weight=1)
frame.columnconfigure(0, weight=1)

timer_label = tk.Label(frame,  text="Time Elapsed: 0 hr 0 min 0 sec", font=label_font, fg="#00FF00", bg="#1C1C1C")
timer_label.grid(row=0, column=0, sticky="nsew", pady=10)

mind_level_label = tk.Label(frame, textvariable=mind_level, font=label_font,fg="#00FF00", bg="#1C1C1C")
mind_level_label.grid(row=1, column=0, sticky="nsew", pady=20)

start_button = tk.Button(frame, text="Start Focus Session", command=run_timer, font=font_style, fg="#39FF14", bg="#1C1C1C", activeforeground="black", activebackground="#39FF14")
start_button.grid(row=2, column=0, sticky="nsew", pady=10)

reset_button = tk.Button(frame,text="Reset Timer", command=reset_timer, font=font_style, fg="#39FF14", bg="#1C1C1C", activeforeground="black", activebackground="#39FF14")
reset_button.grid(row=3, column=0,sticky="nsew", pady=10)

root.mainloop()