cafe = []
cat_num = []

while True:
    inp = input()
    if inp == "MEOW":
        break
    caf = inp.split()[0]
    cafe.append(caf)
    cat = inp.split()[1]
    cat_num.append(int(cat))

print(cafe[cat_num.index(max(cat_num))])
