income = int(input())
if income in range(0, 15528):
    percent = 0
    calculated_tax = int(round(income * percent / 100))
    print("The tax for {} is {}%. That is {} dollars!".format(income,percent, calculated_tax))

elif income in range(15528, 42708):
    percent = 15
    calculated_tax = int(round(income * percent / 100))
    print("The tax for {} is {}%. That is {} dollars!".format(income,percent, calculated_tax))

elif income in range(42708, 132407):
    percent = 25
    calculated_tax = int(round(income * percent / 100))
    print("The tax for {} is {}%. That is {} dollars!".format(income,percent, calculated_tax))

else:
    percent = 28
    calculated_tax = int(round(income * percent / 100))
    print("The tax for {} is {}%. That is {} dollars!".format(income,percent, calculated_tax))
