file = open("./input.txt")

mylines = file.readlines()
total = 0
for i in mylines:
    ints = list(filter(lambda e: e.isdigit(),list(i)))
    total += int(ints[0]+ints[len(ints)-1])
print(total)
file.close()
