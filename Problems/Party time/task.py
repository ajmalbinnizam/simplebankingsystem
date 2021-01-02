guest_list = []
while True:
    guest = input()
    if guest == '.':
        break
    guest_list.append(guest)
print(f'{guest_list}\n{len(guest_list)}')
