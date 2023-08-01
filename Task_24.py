# В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло a[i] ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном списке урожайности грядки.

N = int(input("Введи кол-во кустов на грядке: "))
spisok = list(map(int, input(f"Введи {N} цифр через пробел: ").split()))

N = len(spisok)
spisok = spisok + spisok[:2]
a = 0
for i in range(N):
    a = max(a, spisok[i] + spisok[i + 1] + spisok[i + 2])
print(
    f"Максимальное число ягод, которое может собрать за один заход собирающий модуль: {a}"
)