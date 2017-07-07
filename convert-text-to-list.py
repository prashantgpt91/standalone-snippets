row = []
p = open('med-name.txt', 'r')
for line in p.readlines():
    row.append(line[:-1])

print row
