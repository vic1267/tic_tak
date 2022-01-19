from datetime import datetime
import time

start_time = datetime.now()

s = 0
for a in range(1, 151):
    for b in range(1, 151):
        for c in range(1, 151):
            for d in range(1, 151):
                for e in range(1, 151):
                    if e**5 == a**5 + b**5 + c**5 + d**5:
                        s = a + b + c + d + e
                        print(a, b, c, d, e, 's=', s)
print('_______________________________')


print("Время работы программы", datetime.now() - start_time)



