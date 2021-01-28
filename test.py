d = {}
m = 0
s = ""
with open('input.txt', mode='rt', encoding='utf-8') as f:
    for line in f:
        linesplit = line[:-1].split(':')
        if len(linesplit)==1:
            m = int(linesplit[0])
        else:
            d[int(linesplit[0])] = linesplit[1]

for i in sorted(list(d.keys())):
    if m%i == 0:
        s = s + d[i]
if s == "":
    print(m)
else:
    print(s)