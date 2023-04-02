import tkinter as tk
from tkinter import filedialog


def Filepath():
    root = tk.Tk()
    root.withdraw()

    directory = filedialog.askopenfilename()

    return directory
