in_trans = "translit.txt"
in_rus = "russian.txt"
out_name = "out.txt"


def input_file(in_name):
    file = open(in_name, encoding='utf-8')
    s = file.readline()
    s = s.replace(" ", "").split(",")
    l = []
    for item in s:
        l.append(item)
    return l


def translit_into_english(s, l_trans, l_rus):
    symbols = []
    for symbol in s:
        symbols.append(symbol if symbol not in l_rus else l_trans[l_rus.index(symbol)])
    return "".join(symbols)


def translit_into_russian(s, l_trans, l_rus):
    symbols = []
    for symbol in s:
        symbols.append(symbol if symbol not in l_trans else l_rus[l_trans.index(symbol)])
    return "".join(symbols)


def write_to_file(s):
    with open(out_name, 'w') as f:
        for item in s:
            f.write(item)


if __name__ == "__main__":
    print("Введите текст для перевода:")
    s = input()
    l_trans = input_file(in_trans)
    l_rus = input_file(in_rus)
    print("Транслит:")
    print(l_trans)
    print("Его размер:")
    print(len(l_trans))
    print("Русский:")
    print(l_rus)
    print("Его размер:")
    print(len(l_rus))
    print("Транслитированное слово:")
    print(translit_into_english(s, l_trans, l_rus))
    write_to_file(translit_into_english(s, l_trans, l_rus))