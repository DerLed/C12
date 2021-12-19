import tkinter as tk


class IT14:
    def __init__(self):
        self.H14_list = [
            (1, 250),
            (3, 300),
            (6, 360),
            (10, 430),
            (18, 520),
            (30, 620),
            (50, 740),
            (80, 870),
            (120, 1000),
            (180, 1150),
            (250, 1300),
            (315, 1400),
            (400, 1550)
        ]

        self.h14_list = [
            (1, -250),
            (3, -300),
            (6, -360),
            (10, -430),
            (18, -520),
            (30, -620),
            (50, -740),
            (80, -870),
            (120, -1000),
            (180, -1150),
            (250, -1300),
            (315, -1400),
            (400, -1550)
        ]

        print(self.h14_list[::-1])

    def get_value(self, out_d: int, inner_d: int) -> tuple:
        pr_out_d = 0
        pr_inner_d = 0

        for o_d in self.h14_list[::-1]:
            if out_d >= o_d[0]:
                pr_out_d = abs(o_d[1]) / 1000
                break

        for in_d in self.H14_list[::-1]:
            if inner_d >= in_d[0]:
                pr_inner_d = in_d[1] / 1000
                break
        t_c12 = round((pr_out_d + pr_inner_d)/2, 3)
        return pr_out_d, pr_inner_d, t_c12


class C12Frame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.lbl_D1 = tk.Label(self, text="Наружный диаметр")
        self.lbl_D2 = tk.Label(self, text="Внутрений диаметр")
        self.entry_D1 = tk.Entry(self)
        self.entry_D2 = tk.Entry(self)
        self.btn_calc = tk.Button(self, text="Вычислить", command=self.calc)

        self.lbl_D1.grid(column=0, row=0)
        self.lbl_D2.grid(column=0, row=1)
        self.entry_D1.grid(column=1, row=0)
        self.entry_D2.grid(column=1, row=1)
        self.btn_calc.grid(column=0)

    def calc(self):
        print(self.entry_D1.get())


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("C12 Технологичесая прибавка к толщине")
        self.c12frame = C12Frame(self)
        self.c12frame.pack()


if __name__ == "__main__":
    d = IT14()
    print(d.get_value(159, 142))
    app = App()
    app.mainloop()
