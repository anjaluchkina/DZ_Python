# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

import random

from random import randint

summ_coin = int(input("Введите количество монет: "))

m = 0  # решка
k = 0  # герб
coins = [0, 1]
for i in range(summ_coin):
    random.shuffle(coins)
    print(f"Все монеты {coins}")  # все монетки с вероятностью вверх решка или герб
    if int(coins[0]) == 0:
        k += 1
    if int(coins[0]) == 1:
        m += 1
print(f"Всего монет {m, k}")  # подсчет сколько решки и сколько герба

if m > k:
    ans = k
else:
    ans = m

print(f"Минимальное количество монет, которые нужно перевернуть {ans}")