from datetime import datetime
import time

start_time = datetime.now()
print('Начало выполнения', datetime.now())

e = []
sm = []
for i in range(1, 151):
    e.append(i**5)
sm = [a + b + c + d for a, b, c, d in zip(e, e, e, e)]  #сумма списков

for i in range(1, 151):
    print(sm[i], e[i], i)

for j in range(1, 151):
    if e == sm:
        print(e, sm, j)

print('Завершение работы', datetime.now())
print('_______________________________')
print("Время работы программы", datetime.now() - start_time)
