"""Допускаемое напряжение сталей марок 09Г2С, 16ГС до 32мм"""
mat_09G2S_16GS_up_to_32mm = (
    (20, 196),
    (100, 177),
    (150, 171),
    (200, 165),
    (250, 162),
    (300, 151),
    (350, 140),
    (375, 133),
    (400, 122),
    (410, 104),
    (420, 92),
    (430, 86),
    (440, 78),
    (450, 71),
    (460, 64),
    (470, 56),
    (475, 53),
)

"""Допускаемое напряжение сталей марок 09Г2С, 16ГС свыше 32мм"""
mat_09G2S_16GS_over_32mm = (
    (20, 183),
    (100, 160),
    (150, 154),
    (200, 148),
    (250, 145),
    (300, 134),
    (350, 123),
    (375, 116),
    (400, 105),
    (410, 104),
    (420, 92),
    (430, 86),
    (440, 78),
    (450, 71),
    (460, 64),
    (470, 56),
    (475, 53),
)

mat_list = {
    'Лист 09Г2С, 16ГС до 32 мм': mat_09G2S_16GS_up_to_32mm,
    'Лист 09Г2С, 16ГС свыше 32 мм': mat_09G2S_16GS_over_32mm,
    'Труба 09Г2С': mat_09G2S_16GS_over_32mm
}


def line_interpolate(min_p, max_p, temp):
    x1 = min_p[0]
    x2 = max_p[0]
    f_x1 = min_p[1]
    f_x2 = max_p[1]
    return f_x1 - ((f_x1 - f_x2) * (temp - x1)) / (x2 - x1)


def find_sigma(t, place):
    min_s = None
    max_s = None

    if t < place[0][0]:
        return place[0][1]
    if t > place[-1][0]:
        return False

    for i, tt in enumerate(place):
        if t == place[i][0]:
            return place[i][1]
        if place[i][0] < t < place[i+1][0]:
            min_s = place[i]
            max_s = place[i+1]
            print(min_s, max_s)
            break

    return line_interpolate(min_s, max_s, t)


def calc_test_pressure(calc_pressure, calc_temp, material):
    sigma_20 = find_sigma(20, material)
    sigma_calc = find_sigma(calc_temp, material)
    return 1.25 * calc_pressure * (sigma_20/sigma_calc)
