import time
import tkinter as tk 
from threading import Thread
import pygame

# Initialize the pygame mixer to handle sound effects
pygame.mixer.init()

# Dictionary to map levels to their corresponding sound files
sounds ={
    1: pygame.mixer.Sound("alert/level1.wav"),
    2: pygame.mixer.Sound("alert/level2.wav"),
    3: pygame.mixer.Sound("alert/level3.wav"),
    4: pygame.mixer.Sound("alert/level4.wav"),
    5: pygame.mixer.Sound("alert/level5.wav"),
}
# Function to determine the user's current mental level based on elapsed time
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
    # Play a sound only if the level changes
    if mind_level.get() !=text:
        sounds[level].play()
    
    return text

# Function to start the focus timer
def start_timer():
    global reset_flag
    reset_flag.set(False)
    elapsed_time = 0 
    while elapsed_time <= 180*60 and not reset_flag.get(): # Run until 180 minutes or reset
        time.sleep(1) # Wait for 1 second
        elapsed_time +=1  # Increment elapsed time
        mind_level.set(update_mind_level(elapsed_time))  # Update mind level text
        hours = elapsed_time // 3600 # Calculate hours
        minutes = (elapsed_time % 3600) // 60 # Calculate minutes
        seconds = elapsed_time % 60   # Calculate seconds
        # Update the timer label with formatted time
        timer_label.config(text=f"Time Elapsed : {hours} hr {minutes} min {seconds} sec")
        root.update() # Refresh the GUI

# Function to reset the timer and interface
def reset_timer():
    global reset_flag
    reset_flag.set(True)
    timer_label.config(text="Time Elapsed: 0 hr 0 min 0 sec")
    mind_level.set("Empty mind (level 0)")

# Function to start the timer in a separate thread
def run_timer():
    timer_thread = Thread(target=start_timer)
    timer_thread.daemon = True
    timer_thread.start()

# Create the main Tkinter window
root =tk.Tk()
root.title("Level Up")
root.configure(bg="#1C1C1C")

# Define fonts for the interface
font_style = ("Terminal",12)
label_font = ("Terminal", 16,"bold")

# Variables to hold the mind level text and reset flag
mind_level = tk.StringVar()
mind_level.set("Empty Mind (level 0)")
reset_flag = tk.BooleanVar()

# Create a frame to hold the interface elements
frame = tk.Frame(root, bg="#1C1C1C", bd=5, relief="solid", highlightbackground="green", highlightcolor="green", highlightthickness=2)
frame.pack(pady=20, padx=20, expand=True)

# Configure row and column weights for the frame layout
frame.rowconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)
frame.rowconfigure(2, weight=1)
frame.rowconfigure(3, weight=1)
frame.columnconfigure(0, weight=1)

# Create a label to display the timer
timer_label = tk.Label(frame,  text="Time Elapsed: 0 hr 0 min 0 sec", font=label_font, fg="#00FF00", bg="#1C1C1C")
timer_label.grid(row=0, column=0, sticky="nsew", pady=10)

# Create a label to display the current mind level
mind_level_label = tk.Label(frame, textvariable=mind_level, font=label_font,fg="#00FF00", bg="#1C1C1C")
mind_level_label.grid(row=1, column=0, sticky="nsew", pady=20)

# Create a button to start the focus session
start_button = tk.Button(frame, text="Start Focus Session", command=run_timer, font=font_style, fg="#39FF14", bg="#1C1C1C", activeforeground="black", activebackground="#39FF14")
start_button.grid(row=2, column=0, sticky="nsew", pady=10)

# Create a button to reset the timer
reset_button = tk.Button(frame,text="Reset Timer", command=reset_timer, font=font_style, fg="#39FF14", bg="#1C1C1C", activeforeground="black", activebackground="#39FF14")
reset_button.grid(row=3, column=0,sticky="nsew", pady=10)

# Run the Tkinter main loop to display the interface
root.mainloop()
