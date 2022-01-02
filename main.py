import tkinter as tk
from tkinter import ttk

from C12Frame import C12Frame
from sigma_steel_frame import SigmaSteelFrame


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('520x250')
        self.resizable(width=False, height=False)
        self.title("C12 Технологичесая прибавка к толщине")
        self.tab_control = ttk.Notebook(self)

        self.c12frame = C12Frame(self.tab_control)
        self.tense_steel_frame = SigmaSteelFrame(self.tab_control)

        self.tab_control.add(self.c12frame, text='C12 Технологичесая\nприбавка к толщине')
        self.tab_control.add(self.tense_steel_frame, text='Допускаемые напряжения\nпо ГОСТ Р 34233.1-2017')

        self.tab_control.pack(expand=True, fill='x', anchor='center')

        #self.tense_steel_frame = SigmaSteelFrame(self)
        #self.c12frame.pack()
        #self.tense_steel_frame.pack()


if __name__ == "__main__":
    app = App()
    app.mainloop()
