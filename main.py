import tkinter as tk
from C12Frame import C12Frame


# class IT14:
#     def __init__(self):
#         self.H14_list = [
#             (1, 250),
#             (3, 300),
#             (6, 360),
#             (10, 430),
#             (18, 520),
#             (30, 620),
#             (50, 740),
#             (80, 870),
#             (120, 1000),
#             (180, 1150),
#             (250, 1300),
#             (315, 1400),
#             (400, 1550)
#         ]

# self.h14_list = [
#     (1, -250),
#     (3, -300),
#     (6, -360),
#     (10, -430),
#     (18, -520),
#     (30, -620),
#     (50, -740),
#     (80, -870),
#     (120, -1000),
#     (180, -1150),
#     (250, -1300),
#     (315, -1400),
#     (400, -1550),
#     (500, -1750),
#     (630, -2000),
#     (800, -2300),
#     (1000, -2600),
#     (1250, -3100),
#     (1600, -3700),
#     (2000, -4400),
#     (2500, -5400)

# ]

# print(self.h14_list[::-1])

# def get_value(self, out_d: int, inner_d: int) -> tuple:
#     pr_out_d = 0
#     pr_inner_d = 0

# for o_d in self.h14_list[::-1]:
#     if out_d >= o_d[0]:
#         pr_out_d = abs(o_d[1]) / 1000
#         break

# for in_d in self.H14_list[::-1]:
#     if inner_d >= in_d[0]:
#         pr_inner_d = in_d[1] / 1000
#         break
# t_c12 = round((pr_out_d + pr_inner_d)/2, 3)
# return pr_out_d, pr_inner_d, t_c12


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("C12 Технологичесая прибавка к толщине")
        self.c12frame = C12Frame(self)
        self.c12frame.pack()


if __name__ == "__main__":


    app = App()
    app.mainloop()
