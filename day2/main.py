import sys
import re


def part1(myLines):
    red = 12
    green = 13
    blue = 14
    total = 0
    for line in myLines:
        gameId = re.match(r"Game (\d*):", line).group(1)
        possible = True
        matches = re.finditer(r"(\d*) ([a-zA-z]*)", line)
        for i in matches:
            if i.group(2).lower() == "blue":
                if int(i.group(1)) > blue:
                    possible = False
                    break
            elif i.group(2).lower() == "red":
                if int(i.group(1)) > red:
                    possible = False
                    break
            elif i.group(2).lower() == "green":
                if int(i.group(1)) > green:
                    possible = False
                    break
        if possible:
            total += int(gameId)
    print(f"part1:{total}")


def part2(myLines):
    total = 0
    for line in myLines:
        red = 0
        green = 0
        blue = 0
        matches = re.finditer(r"(\d*) ([a-zA-z]*)", line)
        for i in matches:
            if i.group(2).lower() == "blue":
                if int(i.group(1)) > blue:
                    blue = int(i.group(1))
            elif i.group(2).lower() == "red":
                if int(i.group(1)) > red:
                    red = int(i.group(1))
            elif i.group(2).lower() == "green":
                if int(i.group(1)) > green:
                    green = int(i.group(1))
        total += red * green * blue
    print(f"part2:{total}")


if __name__ == "__main__":
    filename = sys.argv[1]
    file = open(filename)
    mylines = file.read().splitlines()
    file.close()
    part1(mylines)
    part2(mylines)
