import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk

#menu logic

def when_started():
    frame_top.grid_forget()
    frame_middle.grid_forget()
    frame_bottom.grid_forget()

    frame_trainer_name.pack(fill=tk.BOTH,expand=True)
    retrieve_button = tk.Button(frame_trainer_name, text="Done", command=retrieve_text)

    label_trainer_name.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
    trainer_name_entry.place(relx=0.5,rely=0.5,anchor=tk.CENTER)
    retrieve_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

def retrieve_text():
    global trainer_name
    trainer_name = trainer_name_entry.get()
    trainer_name = trainer_name.capitalize()
    frame_trainer_name.forget()
    frame_battle_screen.pack(fill=tk.BOTH, expand=True)
    background_label.lift()
    
    
def init_battle_background(frame, image_path):
    global background_label, original_image
    original_image = Image.open(image_path)
    background_image = ImageTk.PhotoImage(original_image)
    background_label = tk.Label(frame, image=background_image)
    background_label.image = background_image
    background_label.place( x=0, y=0, relwidth=1, relheight=1)
    frame_battle_screen.bind("<Configure>", resize_image)


def resize_image(event):
    global background_image
    new_width = event.width
    new_height = event.height
    image = original_image.resize((new_width, new_height))
    background_image = ImageTk.PhotoImage(image)
    background_label.config(image=background_image)

    
def init_menu(window):
    global frame_top, frame_middle, frame_bottom, frame_trainer_name, label_trainer_name, trainer_name_entry, frame_battle_screen

    frame_top = tk.Frame(window, bg="red", width=200, height=100)
    frame_middle = tk.Frame(window, bg="black",width=200, height=20)
    frame_bottom = tk.Frame(window, bg="white", width=200, height=100)

    frame_top.grid(row=0, column=0, sticky="nsew")
    frame_middle.grid(row=1, column=0, sticky="ew")
    frame_bottom.grid(row=2, column=0, sticky="nsew")

    window.grid_rowconfigure(0, weight=1)  # Top row
    window.grid_rowconfigure(1, weight=0)  # Middle row
    window.grid_rowconfigure(2, weight=1)  # Bottom row
    window.grid_columnconfigure(0, weight=1)  # Column 0 (only column)
    custom_font_path = "retro_font.ttf"
    retro_font = font.Font(family="VCR OSD Mono",size=12,weight="bold")
 

    start_button = tk.Button(frame_middle, text="Start Game: ", font=retro_font, fg="black", bg="Green", command=when_started)
    start_button.pack()

    label = tk.Label(frame_top, text="Pokemon Duel Simulator",font=retro_font, bg="red")
    label.pack(padx=20,pady=20)

    frame_trainer_name = tk.Frame(window, bg="#FFFFED")
    label_trainer_name = tk.Label(frame_trainer_name,text="Hello Trainer... What would you like to be called?", font=retro_font, bg="#FFFFED")

    trainer_name_entry = tk.Entry(frame_trainer_name, width=30, bd=2, relief=tk.SOLID)
   
    frame_trainer_name.pack_forget()
    label_trainer_name.place_forget()
    trainer_name_entry.place_forget()

    frame_battle_screen = tk.Frame(window)
    init_battle_background(frame_battle_screen, "pokemon_battle_background.jpg")
