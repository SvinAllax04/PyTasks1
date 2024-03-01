class Sweets():
    multiplication = lambda x, y: x * y
    def __init__(self, name, cost_per_kg):
        self.name = name
        self.cost_per_kg = cost_per_kg

    def build(self):
        print("Стоимость конфеты " + self.name + " за килограмм равна - " + str(self.cost_per_kg))

    def get_cost(self):
        return self.cost_per_kg

    def calculate(*sweet: object, money, full_sum_sweets):
        i = 0
        while money >= full_sum_sweets:
            money -= *sweet.cost_per_kg
            i += 1
        return money, i