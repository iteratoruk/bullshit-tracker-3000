import tkinter as tk
from .ui import BullshitTrackerUI


def main():
    root = tk.Tk()
    BullshitTrackerUI(root)
    root.mainloop()
