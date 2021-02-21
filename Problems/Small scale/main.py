nums = []
while True:
    num = input()
    if num == ".":
        break
    nums.append(float(num))

print(min(nums))
