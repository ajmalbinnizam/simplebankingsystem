# put your python code here
d = int(input())
food = int(input())
flight = int(input())
hotel = int(input())
total = ((food * d) + (flight * 2) + (hotel * (d -1)))
print(total)