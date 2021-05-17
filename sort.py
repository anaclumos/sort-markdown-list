file = open('techs.md', 'r')
lines = file.readlines()

count = 0
postlist = []

for line in lines:
    postlist.append(line)


postlist.sort()

for line in postlist:
    print(line.strip())
