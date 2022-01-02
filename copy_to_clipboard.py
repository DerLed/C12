import tkinter as tk


def copy_to_clipboard(value):
    r = tk.Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(str(value))
    r.destroy()
    return True
