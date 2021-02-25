# # Write your code here
# #Design
# """
# 1. Every person can create 1 or more objects
# 2. Every object will have all the methods and data relevant for that object.
# 3. Data will consist of dict of card numbers (400000 + 9 digit account number + 0)
# and corresponding PINs
# 3.a Account number can be derived from the card number
# 3.b Every object will have 0 or more card numbers
# 4. Every object will start with a dict of 0 cards
# 4b. These objects can be modified through the instance methods
# """
#
#
# # Write your code here
# class BankingAccount(object):
#     def __init__(self):
#         self.cardmasterdata = {}
#         self.accountnumberlist = ["000000000"]
#         self.cardnumber = None
#
#     def createcard(self):
#         import random
#         newaccountint = int(max(self.accountnumberlist)) + 1
#         newaccountchar = f"{newaccountint:09d}"
#         #Append new account to the master account list
#         self.accountnumberlist.append(newaccountchar)
#         #Create the new cardnumber
#         cardnumber = "400000" + newaccountchar + "0"
#         pin = str(random.randint(1000, 9999))
#         #Append new card to the cardmasterdata. Also, map it to its pin
#         self.cardmasterdata[cardnumber] = pin
#         return (cardnumber, pin)
#
#     def loginaccount(self, cardnumber, pin):
#         self.cardnumber = cardnumber
#         if cardnumber in self.cardmasterdata.keys() and self.cardmasterdata[cardnumber] == pin:
#             print("You have successfully logged in!\n")
#             while True:
#                 print("1. Balance\n2. Log out\n0. Exit")
#                 logininput = input()
#                 if logininput == "1":
#                     print("Balance: 0")
#                 elif logininput == "2":
#                     print("You have successfully logged out!")
#                     break
#                 elif logininput == "0":
#                     print("Bye")
#                     exit()
#         else:
#             print("Wrong card number or PIN!")
#
#
# ###Actual start of program
# #Create an object in the beginning. The same object will be used throughout the program
# BankingAccountObject1 = BankingAccount()
# while True:
#     print("1. Create an account \n2. Log into account\n0. Exit")
#     userinput = input()
#     if userinput == "1":
#         currentcardnumber, currentpin = BankingAccountObject1.createcard()
#         print(f"Your card has been created\nYour card number:\n{currentcardnumber}")
#         print(f"Your card PIN:\n{currentpin}")
#     elif userinput == "2":
#         print("Enter your card number:")
#         cardnumber = input()
#         print("Enter your PIN:")
#         pin = input()
#         BankingAccountObject1.loginaccount(cardnumber, pin)
#     elif userinput == "0":
#         print("Bye!")
#         break
#
# exit()

import random
from string import digits
import sqlite3 as sq


class BankSystem:
    prompt1 = '1. Create an account\n2. Log into account\n0. Exit\n'
    prompt2 = '1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log out\n0. Exit\n'
    prompt3 = 'You have successfully logged in!\n'
    prompt4 = 'Wrong card number or PIN!\n'
    prompt5 = 'Enter your card number:\n'
    prompt6 = 'Enter your PIN:\n'
    prompt7 = 'Your card number:>'
    prompt8 = 'Your card PIN:'
    prompt9 = 'Your card has been created'
    prompt10 = 'Wrong choice'
    prompt11 = 'You have successfully logged out!\n'
    prompt12 = 'Enter income:\n'
    prompt13 = 'Income was added!\n'
    prompt14 = 'The account has been closed!\n'
    IIN = '400000'
    logged_card = None

    @staticmethod
    def input(prompt):
        action = input(prompt)
        return action

    @staticmethod
    def checksum_lhun(string):
        digit = list(map(int, string))
        odd_sum = sum(digit[-1::-2])
        even_sum = sum([sum(divmod(2 * d, 10)) for d in digit[-2::-2]])
        return (odd_sum + even_sum) % 10

    def verify_card(self, number):
        return self.checksum_lhun(number) == 0

    def generate_lhun(self, string):
        #  Generate the Luhn check digit to append to the provided string.
        cksum = self.checksum_lhun(string + '0')
        return str((10 - cksum) % 10)

    def append_lhun(self, string):
        #  Append Luhn check digit to the end of the provided string
        return string + str(self.generate_lhun(string))

    def main_menu(self):
        while True:
            action = input(self.prompt1)
            if action == '1':
                self.create_card()
            elif action == '2':
                self.login()
            elif action == '0':
                print('Bye!')
                conn.close()
                exit()

    def create_card(self):
        card_number = self.generate_number()
        card_pin = self.generate_pin()
        user_id = random.randint(0, 1000000)
        print('{}\n{}\n{}\n{}\n{}'.format(self.prompt9, self.prompt7, card_number, self.prompt8, card_pin))
        cur.execute("""INSERT INTO card VALUES (?, ?, ?, ?)""", (user_id, card_number, card_pin, 0))
        conn.commit()

    def generate_number(self):
        number = self.IIN
        for i in range(9):
            number += random.choice(digits)
        number += self.generate_lhun(number)
        return number

    @staticmethod
    def generate_pin():
        pin = ''
        for i in range(4):
            pin += random.choice(digits)
        return pin

    def login(self):
        card_number = self.input(self.prompt5)
        card_pin = self.input(self.prompt6)
        cur.execute("""SELECT number, pin FROM card WHERE number=:number""", {"number": card_number})
        if (card_number, card_pin) == cur.fetchone():
            self.logged_card = card_number
            print(self.prompt3)
            self.account_action()
        else:
            print(self.prompt4)

    def balance(self):
        cur.execute("""SELECT balance FROM card WHERE number=:number""", {"number": self.logged_card})
        balance = cur.fetchone()
        print(f'Balance: ', balance[0])

    def add_income(self):
        income = int(self.input(self.prompt12))
        cur.execute("""UPDATE card SET balance = balance +? WHERE number=?""", (income, self.logged_card))
        conn.commit()
        print(self.prompt13)

    def account_action(self):
        while True:
            print(self.prompt2)
            action = input()
            if action == '1':
                self.balance()
            elif action == '2':
                self.add_income()
            elif action == '3':
                self.transfer_main()
            elif action == '4':
                self.close_account()
                break
            elif action == '5':
                self.logged_card = None
                print(self.prompt11)
                break
            elif action == '0':
                print('\nBye!')
                conn.close()
                exit()

    def close_account(self):
        cur.execute("""DELETE FROM card 
                        WHERE number=:number""", {"number": self.logged_card})
        conn.commit()
        self.logged_card = None
        print(self.prompt14)

    def transfer_main(self):
        print('Transfer')
        card_input = input('Enter card number:\n')
        if self.check_transfer(card_input) is True:
            amount = int(input('Enter how much money you want to transfer:\n'))
            if self.check_transfer_balance(amount) is True:
                self.make_transaction(card_input, amount)

    def check_transfer(self, number):
        if self.verify_card(number) is True:
            if self.check_card_in_db(number) is True:
                return True
            else:
                print('Such a card does not exist.\n')
                return False
        else:
            print('Probably you made mistake in the card number. Please try again!\n')
            return False

    def check_transfer_balance(self, amount):
        cur.execute("""SELECT balance FROM card WHERE number=:number""", {"number": self.logged_card})
        balance = cur.fetchone()
        if amount <= balance[0]:
            return True
        else:
            print('Not enough money!\n')

    @staticmethod
    def check_card_in_db(number):
        cur.execute("""SELECT number FROM card WHERE number=:number""", {"number": number})
        if cur.fetchone() is not None:
            return True

    def make_transaction(self, number_to, amount):
        cur.execute("""UPDATE card SET balance = balance +? WHERE number=?""", (amount, number_to))
        cur.execute("""UPDATE card SET balance = balance -? WHERE number=?""", (amount, self.logged_card))
        conn.commit()
        print('Success!\n')


conn = sq.connect('card.s3db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS card 
                (
                id INTEGER,
                number TEXT,
                pin TEXT,
                balance INTEGER DEFAULT 0
                )""")
BankSystem().main_menu()