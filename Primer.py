from datetime import datetime
import time

start_time = datetime.now()
print('Начало выполнения', datetime.now())

s = 0
for a in range(25, 151):
    for b in range(1, 151):
        for c in range(1, 151):
            for d in range(1, 151):
                for e in range(1, 151):
                    if e**5 == a**5 + b**5 + c**5 + d**5:
                        s = a + b + c + d + e
                        print(a, b, c, d, e, 's=', s)
print('_______________________________')

# (27**5 + 84**5 + 110**5 + 133**5)**0.2
# 144.00000000000003

print('Завершение работы', datetime.now())
print('_______________________________')
print("Время работы программы", datetime.now() - start_time)



