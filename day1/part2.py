import re
file = open("./input.txt")

mylines = file.readlines()
total = 0
for i in mylines:
    line = i
    rep = {'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    rep = dict((re.escape(k), v) for k, v in rep.items())
    for k, v in rep.items():
        locs = re.finditer(k,line)
        for x in locs:
            listStr = list(line)
            listStr[x.start()+1] = v
            line = ''.join(listStr)
    ints = list(filter(lambda e: e.isdigit(),list(line)))
    if(len(ints) > 1):
        total += int(ints[0]+ints[len(ints)-1])
    else:
        total += int(ints[0]+ints[0])
print(total)
file.close()
