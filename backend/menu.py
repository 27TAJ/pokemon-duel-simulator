import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
from pokemon import get_pokemon_image, init_teams

def when_started(window):
    frame_top.grid_forget()
    frame_middle.grid_forget()
    frame_bottom.grid_forget()

    frame_trainer_name.pack(fill=tk.BOTH,expand=True)
    retrieve_button = tk.Button(frame_trainer_name, text="Done",command=lambda: retrieve_text(window))

    label_trainer_name.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
    trainer_name_entry.place(relx=0.5,rely=0.5,anchor=tk.CENTER)
    retrieve_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

def retrieve_text(window):
    global trainer_name, frame_battle_screen
    trainer_name = trainer_name_entry.get()
    trainer_name = trainer_name.capitalize()
    frame_trainer_name.forget()
    frame_battle_screen = tk.Frame(window)
    frame_battle_screen.pack(fill=tk.BOTH, expand=True)
    init_battle_background(frame_battle_screen, "pokemon_battle_background.jpg")
    
def init_battle_background(frame, image_path):
    global background_image, original_image, canvas, sprite_images
    
    original_image = Image.open(image_path)
    background_image = ImageTk.PhotoImage(original_image)

    canvas = tk.Canvas(frame, width=frame.winfo_width(), height=frame.winfo_height())
    canvas.create_image(0, 0, anchor=tk.NW, image=background_image)
    canvas.image = background_image
    canvas.place(x=0, y=0, relwidth=1, relheight=1)
    frame_battle_screen.bind("<Configure>", resize_image)

    trainer_team, enemy_team = init_teams()
    sprite_images = []


    for index, pokemon in enumerate(trainer_team):
        pokemon_image = get_pokemon_image(pokemon)
        sprite_image = ImageTk.PhotoImage(pokemon_image)
        sprite_images.append(sprite_image)
        x = 100 + (index*100)
        y = 400
        label = tk.Label(frame_battle_screen, image=sprite_image)
        label.image = sprite_image
        label.place(x=x,y=y, anchor=tk.SE)
        

    for index, pokemon in enumerate(enemy_team):
        pokemon_image = get_pokemon_image(pokemon)
        sprite_image = ImageTk.PhotoImage(pokemon_image)
        sprite_images.append(sprite_image)
        x = 700 - (index * 100)
        y = 100
        label = tk.Label(frame_battle_screen, image=sprite_image)
        label.image = sprite_image
        label.place(x=x,y=y, anchor=tk.SE)

def resize_image(event):
    global background_image
    new_width = event.width
    new_height = event.height
    image = original_image.resize((new_width, new_height))
    background_image = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, anchor=tk.NW, image= background_image)
    canvas.image = background_image

    
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
    window.grid_columnconfigure(0, weight=1)
    custom_font_path = "retro_font.ttf"
    retro_font = font.Font(family="VCR OSD Mono",size=12,weight="bold")
 

    start_button = tk.Button(frame_middle, text="Start Game: ", font=retro_font, fg="black", bg="Green", command=lambda:when_started(window))
    start_button.pack()

    label = tk.Label(frame_top, text="Pokemon Duel Simulator",font=retro_font, bg="red")
    label.pack(padx=20,pady=20)

    frame_trainer_name = tk.Frame(window, bg="#FFFFED")
    label_trainer_name = tk.Label(frame_trainer_name,text="Hello Trainer... What would you like to be called?", font=retro_font, bg="#FFFFED")

    trainer_name_entry = tk.Entry(frame_trainer_name, width=30, bd=2, relief=tk.SOLID)
   
    frame_trainer_name.pack_forget()
    label_trainer_name.place_forget()
    trainer_name_entry.place_forget()
