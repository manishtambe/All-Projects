import tkinter as tk
import tkcap
from pyscreenshot import grab

root = tk.Tk()
root.geometry("620x700+360+10")
root.resizable(0,0)
root.overrideredirect(True)

from tkinter import simpledialog

ROOT = tk.Tk()

ROOT.withdraw()
# the input dialog
USER_INP = simpledialog.askstring(title="Test",
                                  prompt="What's your Name?:")

# check it out
print("Hello", USER_INP)

root.mainloop()