import tkinter as tk
from menu import init_menu


window = tk.Tk()
window.title("Pokemon Duel Simulator")

init_menu(window)
window.geometry("600x500")
window.mainloop()
