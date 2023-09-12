import tkinter as tk
from tkinter import simpledialog

ROOT = tk.Tk()

ROOT.withdraw()

def simple_gui_input(text):
    return simpledialog.askstring(title="GUI창",
                                    prompt=text)
