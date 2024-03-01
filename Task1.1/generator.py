import random


def rnd_list(a, b, c, l):
    for i in range(c):
        num = random.randint(a, b)
        l.append(num)
    return l

a = 1
b = 100
c = 20
l = []
print(rnd_list(a, b, c, l))
