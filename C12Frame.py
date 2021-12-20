import tkinter as tk
from IT14_tolerance import IT14_TOLERANCE as IT14
from IT14_tolerance import MAX_DIAMETER, MIN_DIAMETER

t_c12 = 0


class C12Frame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.lbl_D1 = tk.Label(self, text="Наружный диаметр")
        self.lbl_D2 = tk.Label(self, text="Внутрений диаметр")
        self.statusbar = tk.Label(self, text="…", bd=1, relief=tk.SUNKEN, anchor=tk.W)

        self.entry_D1 = tk.Entry(self, justify="right")
        self.entry_D2 = tk.Entry(self)

        self.btn_calc = tk.Button(self, text="Вычислить", command=self.calc)
        self.btn_to_clipboard = tk.Button(self, text="Скопировать в буфер", command=self.to_clipboard)

        self.result = tk.Label(self, text="", height=6, justify=tk.LEFT)

        self.entry_D1.bind('<Return>', lambda event: self.entry_D2.focus())
        self.entry_D1.bind('<KP_Enter>', lambda event: self.entry_D2.focus())
        self.entry_D2.bind('<Return>', self.set_focus_copy)
        self.entry_D2.bind('<KP_Enter>', self.set_focus_copy)
        self.btn_to_clipboard.bind('<Return>', lambda event: self.to_clipboard())
        self.btn_to_clipboard.bind('<KP_Enter>', lambda event: self.to_clipboard())

        self.lbl_D1.grid(column=0, row=0)
        self.lbl_D2.grid(column=0, row=1)
        self.entry_D1.grid(column=1, row=0)
        self.entry_D2.grid(column=1, row=1)
        self.btn_calc.grid(column=0, row=2, sticky="WE")
        self.btn_to_clipboard.grid(column=1, row=2)
        self.result.grid(column=0, columnspan=2)
        self.statusbar.grid(column=0, columnspan=2, sticky="WE")

        self.entry_D1.focus()

    def calc(self):
        global t_c12
        tolerance_out_d = 0
        tolerance_inner_d = 0
        try:
            out_d = float(self.entry_D1.get())
            inner_d = float(self.entry_D2.get())
        except ValueError:
            self.entry_D1.delete(0, tk.END)
            self.entry_D2.delete(0, tk.END)
            self.statusbar["text"] = "Вводите в поля только цифры"
            return

        if out_d > MAX_DIAMETER:
            self.statusbar["fg"] = 'red'
            self.statusbar["text"] = "Диаметры от 1мм до 3150мм"
            return
        elif not out_d:
            self.statusbar["fg"] = 'red'
            self.statusbar["text"] = "Вы не ввели одно или оба значений"
            return
        else:
            for o_d in IT14[::-1]:
                if out_d >= o_d[0]:
                    tolerance_out_d = o_d[1] / 1000
                    break

        if inner_d < MIN_DIAMETER:
            self.statusbar["fg"] = 'red'
            self.statusbar["text"] = "Диаметры от 1мм до 3150мм"
            return
        elif not inner_d:
            self.statusbar["fg"] = 'red'
            self.statusbar["text"] = "Вы не ввели одно или оба значений"
            return
        else:
            for in_d in IT14[::-1]:
                if inner_d >= in_d[0]:
                    tolerance_inner_d = in_d[1] / 1000
                    break

        t_c12 = round((tolerance_out_d + tolerance_inner_d)/2, 3)
        print(tolerance_out_d, tolerance_inner_d, t_c12)
        self.result["text"] = f'Наружный диаметр: Da = {out_d} мм\n' \
                              f'Допуск на наружный диаметр: {tolerance_out_d} мм\n' \
                              f'Внутренний диаметр: Da = {inner_d} мм\n' \
                              f'Допуск на внутренний диаметр: {tolerance_inner_d} мм\n' \
                              f'Толщина стенки: S = {(out_d-inner_d)/2} мм\n' \
                              f'Технологическая прибавка: С = {t_c12} мм'
        self.statusbar["fg"] = 'black'
        self.statusbar["text"] = "..."
        self.entry_D1.delete(0, tk.END)
        self.entry_D2.delete(0, tk.END)

    def to_clipboard(self):
        global t_c12
        if t_c12:
            print(t_c12)
            r = tk.Tk()
            r.withdraw()
            r.clipboard_clear()
            r.clipboard_append(str(t_c12))
            r.destroy()
            self.statusbar["fg"] = 'green'
            self.statusbar["text"] = f"Скопировано в буфер: {t_c12}"
            t_c12 = 0
        else:
            self.statusbar["fg"] = 'black'
            self.statusbar["text"] = f"Копировать нечего"

    def set_focus_copy(self, event):
        self.calc()
        self.btn_to_clipboard.focus_set()