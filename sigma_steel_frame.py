import tkinter as tk
from tkinter import ttk
from gost_r_34233_1 import mat_list, find_sigma, calc_test_pressure


class SigmaSteelFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # ---label---
        self.lbl_title = tk.Label(self, text="Допускаемые напряжения по ГОСТ Р 34233.1-2017")
        self.lbl_temp_calc = tk.Label(self, text="Расчетная температура стенки, ºС")
        self.lbl_steel_mark = tk.Label(self, text="Материал")
        self.lbl_calc_pressure = tk.Label(self, text="Расчетное давление, МПа")
        self.result = tk.Label(self, text="", height=6, justify=tk.LEFT)

        # ---entry---
        self.entry_temp_calc = tk.Entry(self, justify="right")
        self.entry_pressure_calc = tk.Entry(self, justify="right")

        # ---combobox---
        self.combo_steel_mark_list = ttk.Combobox(self, values=list(mat_list.keys()))

        # ---button---
        self.btn_calc = tk.Button(self, text="Вычислить", command=self.calc_sigma_steel)

        # ---render---
        self.lbl_title.grid(column=0, columnspan=2)
        self.lbl_temp_calc.grid(column=0, row=1)
        self.entry_temp_calc.grid(column=1, row=1)
        self.lbl_steel_mark.grid(column=0, row=2)
        self.combo_steel_mark_list.grid(column=1, row=2)

        self.lbl_calc_pressure.grid(column=0, row=3)
        self.entry_pressure_calc.grid(column=1, row=3)

        self.btn_calc.grid(column=0, columnspan=2)
        self.result.grid(column=0, columnspan=2)

    def calc_sigma_steel(self):
        try:
            temp_calc = int(self.entry_temp_calc.get())
            pressure_calc = float(self.entry_pressure_calc.get())
            select_mat = self.combo_steel_mark_list.get()
        except ValueError:
            self.entry_temp_calc.delete(0, tk.END)
            self.result["text"] = "Проверьте введеные данные"
            return

        data_mat = mat_list[select_mat]
        ans_temp = find_sigma(temp_calc, data_mat)
        test_pressure = round(calc_test_pressure(pressure_calc, temp_calc, data_mat), 2)
        text_test_pressure = f'{test_pressure} ({round(test_pressure*10, 1)})'.replace('.', ',')
        if ans_temp:
            self.result["text"] = f'Марка стали {select_mat}\n' \
                                  f'Расчетная температура Т = {temp_calc} ºС\n' \
                                  f'Допускаемое напряжение [σ] = {ans_temp} МПа\n' \
                                  f'Пробное давление МПа(кгс/см*2) = {text_test_pressure}'
        else:
            self.result["text"] = f'Проверьте введеные данные'
        print(ans_temp, test_pressure)