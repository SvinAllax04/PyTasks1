import calendar

in_name = "in.txt"
out_name = "out.txt"


def input_file():
    file = open(in_name, encoding='utf-8')
    s = file.readline()
    s = s.replace(" ", "").split(",")
    l = []
    for item in s:
        l.append(int(item))
    return l


def find_days():
    l = input_file()
    month = l[0]
    year = l[1]

    cal = calendar.Calendar()
    weeks = cal.monthdayscalendar(year, month)

    return weeks


def write_to_file(weeks):
    with open(out_name, 'w') as f:
        for week in weeks:
            f.write(','.join(map(str, week)))
            f.write('\n')


if __name__ == '__main__':
    weeks = find_days()
    write_to_file(weeks)
