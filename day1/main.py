import re
import sys


def part1(myLines):
    total = 0
    for i in myLines:
        ints = list(filter(lambda e: e.isdigit(), list(i)))
        total += int(ints[0] + ints[len(ints) - 1])

    print(f"part 1:{total}")


def part2(myLines):
    total = 0
    for i in myLines:
        line = i
        rep = {
            "zero": "0",
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9",
        }
        rep = dict((re.escape(k), v) for k, v in rep.items())
        for k, v in rep.items():
            locs = re.finditer(k, line)
            for x in locs:
                listStr = list(line)
                listStr[x.start() + 1] = v
                line = "".join(listStr)
        ints = list(filter(lambda e: e.isdigit(), list(line)))
        if len(ints) > 1:
            total += int(ints[0] + ints[len(ints) - 1])
        else:
            total += int(ints[0] + ints[0])
    print(f"part 2:{total}")


if __name__ == "__main__":
    filename = sys.argv[1]
    file = open(filename)
    mylines = file.read().splitlines()
    file.close()
    part1(mylines)
    part2(mylines)
