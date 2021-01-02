sq = []
to = []
while True:
    n = int(input())
    sq.append(n * n)
    m = 0
    to.append(n + m)
    squ = sum(sq)
    tot = sum(to)
    if tot == 0:
        break
print(squ)
