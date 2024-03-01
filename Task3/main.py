from Sweets import Sweets

in_file = "in.txt"
out_file = "out.txt"

money = 2051
full_sum_sweets = 301
i = 0


def input_file(in_name):
    file = open(in_name, "r", encoding='utf-8')
    s = file.readlines()
    s = s.replace(" ", "").split(",")
    l = []
    for item in s:
        l.append(item)
    return l


def calculate(sweet, money):
    i = 0
    while money >= full_sum_sweets:
        money -= sweet.cost_per_kg
        i+=1
    return money, i


sweet1 = Sweets("Ромашка", 100)
sweet2 = Sweets("Ласточка", 50)
sweet3 = Sweets("Рафаэлка", 151)
Sweets.calculate(sweet1, sweet2, sweet3, money, full_sum_sweets)
'''print(calculate(sweet3,int(input())))
sweet3.build()
full_sum_sweets -= sweet3.cost_per_kg
print(calculate(sweet1,int(input())))
sweet1.build()
full_sum_sweets -= sweet1.cost_per_kg
print(calculate(sweet2,int(input())))
sweet2.build()'''

'''while money >= full_sum_sweets:
    i+=1
    print(i)
    print(calculate(sweet1,money))'''
