import random


def rnd_list(a, b, c, l):
    for i in range(c):
        num = random.randint(a, b)
        l.append(num)


def count_num(list_in, dict_in):
    for i in list_in:
        if i in dict_in:
            dict_in[i] += 1
        else:
            dict_in[i] = 1


def str_ref(out=""):
    d = {}
    l = []
    file = open('in.txt', encoding='utf-8')
    s = file.readline()
    s = s.replace("[", "")
    s = s.replace("]", "")
    s = s.replace(" ", "")
    s = s.split(",")

    for i in s:
        l.append(int(i))

    count_num(l, d)

    out += "Список:\n" + str(l) + "\n"
    for item in d:
        if d[item] % 2 == 0:
            out += "Количество чётных элементов:\n"
            out += f"'{item}': {d[item]}"
            print(out)

    file.close()
    return out


def write_to_file(out):
    file = open('out.txt', 'w', encoding='utf-8')
    file.write(out)
    file.close()


if __name__ == "__main__":
    out = str_ref()
    write_to_file(out)