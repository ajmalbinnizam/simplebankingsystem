# Write your code here
#Design
"""
1. Every person can create 1 or more objects
2. Every object will have all the methods and data relevant for that object.
3. Data will consist of dict of card numbers (400000 + 9 digit account number + 0)
and corresponding PINs
3.a Account number can be derived from the card number
3.b Every object will have 0 or more card numbers
4. Every object will start with a dict of 0 cards
4b. These objects can be modified through the instance methods
"""


# Write your code here
class BankingAccount(object):
    def __init__(self):
        self.cardmasterdata = {}
        self.accountnumberlist = ["000000000"]
        self.cardnumber = None

    def createcard(self):
        import random
        newaccountint = int(max(self.accountnumberlist)) + 1
        newaccountchar = f"{newaccountint:09d}"
        #Append new account to the master account list
        self.accountnumberlist.append(newaccountchar)
        #Create the new cardnumber
        cardnumber = "400000" + newaccountchar + "0"
        pin = str(random.randint(1000, 9999))
        #Append new card to the cardmasterdata. Also, map it to its pin
        self.cardmasterdata[cardnumber] = pin
        return (cardnumber, pin)

    def loginaccount(self, cardnumber, pin):
        self.cardnumber = cardnumber
        if cardnumber in self.cardmasterdata.keys() and self.cardmasterdata[cardnumber] == pin:
            print("You have successfully logged in!\n")
            while True:
                print("1. Balance\n2. Log out\n0. Exit")
                logininput = input()
                if logininput == "1":
                    print("Balance: 0")
                elif logininput == "2":
                    print("You have successfully logged out!")
                    break
                elif logininput == "0":
                    print("Bye")
                    exit()
        else:
            print("Wrong card number or PIN!")


###Actual start of program
#Create an object in the beginning. The same object will be used throughout the program
BankingAccountObject1 = BankingAccount()
while True:
    print("1. Create an account \n2. Log into account\n0. Exit")
    userinput = input()
    if userinput == "1":
        currentcardnumber, currentpin = BankingAccountObject1.createcard()
        print(f"Your card has been created\nYour card number:\n{currentcardnumber}")
        print(f"Your card PIN:\n{currentpin}")
    elif userinput == "2":
        print("Enter your card number:")
        cardnumber = input()
        print("Enter your PIN:")
        pin = input()
        BankingAccountObject1.loginaccount(cardnumber, pin)
    elif userinput == "0":
        print("Bye!")
        break

exit()
