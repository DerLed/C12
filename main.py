import tkinter as tk
from C12Frame import C12Frame
from sigma_steel_frame import SigmaSteelFrame


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("C12 Технологичесая прибавка к толщине")
        self.c12frame = C12Frame(self)
        self.tense_steel_frame = SigmaSteelFrame(self)
        self.c12frame.pack()
        self.tense_steel_frame.pack()


if __name__ == "__main__":
    app = App()
    app.mainloop()
