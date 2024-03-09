colors = [(0, 'Ультрафиолетовый'), (380, 'Фиолетовый'), (450, 'Синий'), (495, 'Зелёный'),
    (570, 'Жёлтый'), (590, 'Оранжевый'), (620, 'Красный')]

from bisect import bisect_left
w = float(input('Длина волны: '))
p = min(bisect_left(colors, (w,)), len(colors) - 1)
i = p if colors[p][0] <= w else p - 1
print(colors[i][1])
