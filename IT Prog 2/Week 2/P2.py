# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 14:20:53 2018

@author: Romeo
"""
import threading
import time

class BankAccount:
    def __init__(self, currency, first , last, accounttype = "S" , balance = 0, age = 99):
        self.first = first
        self.last = last
        self.balance = balance
        self.currency = currency
        self.acctype = accounttype
        self.age = age
        if self.age > 26:
            self.acctype = "S"
    def Deposit(self, amount):
        if amount < 0:
            return "invalid amount entered"
        else:
            self.balance = self.balance + amount
            return '{} {}'.format("New Balance:", self.balance)
    
    def Withdraw(self, amount):
        if self.acctype == "Y":
            self.balance -= amount
            return '{} {} \n{} {}'.format("Amount withdrawn:", amount,"New Balance:", self.balance)
        else:
            if amount > self.balance:
                self.balance -= amount*1.02
                return '{} {} \n {} {}'.format("Amount withdrawn:", amount,"New Balance:", self.balance)
            else:
                self.balance -= amount
                return '{} {} \n{} {}'.format("Amount withdrawn:", amount,"New Balance:", self.balance)
    
    def Interest(self, interest = 0.01):
        if self.acctype == "Y":
            self.balance = self.balance * (1+interest)
            return self.balance
        else:
            self.balance = self.balance * (1+interest)
            return self.balance

    def Owner(self):
        return '{} {}'.format(self.first, self.last)
    
    def Currency(self):
        return '{} {}'.format("Account Currency:", self.currency)
    
    def Balance(self):
        return '{} {}'.format("Current Balance:", self.balance)
    
    def Accounttype(self):
        if self.acctype == "Y":
            return '{} {}'.format("Account Type:", "Youth Account")
        else:
            return '{} {}'.format("Account Type:", "Savings Account")
    
    def handoff(self):
        return self.balance

 


    
    
accdata  = [["CHF","Romeo","Moritzi","S",75100],["USD","Hans","Ruedi","S",100],["CHF","Kaspar","li","Y",15000],["Fish","Pin","Gu","Y",18]]
while True:
    print("Welcome")
    print("1 - Existing Accounts")
    print("2 - New Account")
    print("3 - Exit")
    start = int(input("Selection: "))
    if start == 1:
        number = 1
        for n in accdata:
            print(number, " - " '{} {}'.format(n[1],n[2]))
            number += 1
        print("Which account would you like to Access? ")
        number = int(input("Selection: "))
        number -= 1
        try:
            curacc = BankAccount(accdata[number][0],accdata[number][1],accdata[number][2],accdata[number][3],accdata[number][4])
            while True:
                print("What would you like to do?")
                print("1 - Deposit")
                print("2 - Whitdraw")
                print("3 - Check Balance")
                print("4 - Information")
                print("5 - Delete Account")
                print("6 - Back")
                secM = int(input("Selection: "))
                if secM == 1:
                    time.sleep(.5)
                    choice = int(input("Amount: "))
                    print(BankAccount.Deposit(curacc ,choice))
                elif secM == 2:
                    time.sleep(.5)
                    choice = int(input("Amount: "))
                    print(BankAccount.Withdraw(curacc,choice))              
                elif secM == 3:
                    time.sleep(.5)
                    print("Current Balance")
                    print(BankAccount.Balance(curacc))
                elif secM == 4:
                    time.sleep(.5)
                    print("Owner")
                    print(BankAccount.Owner(curacc))
                    print(BankAccount.Currency(curacc))
                    print(BankAccount.Accounttype(curacc))
                elif secM == 5:
                    time.sleep(.5)
                    print('Are you sure? Type "YES" to permanently delete the account')
                    conf = input()
                    if conf == "YES":
                        accdata.pop(number)
                        print("Account was deleted")
                        break
                    else:
                        print("Account was not deleted")
                elif secM == 6:
                    print("Exiting current Menu")
                    time.sleep(.5)
                    accdata[number][4] = BankAccount.handoff(curacc)
                    break
                else:
                    print("Input not recognised, try again")
        except IndexError:
            print("Invalid Entry")
            pass
    elif start == 2:
        while True:
            print("What type of account would you like to open")
            print("1 for Savings Account")
            print("2 for YouthAccount")
            print("3 for Exit")
            mainM = int(input("Selection: "))
            if mainM == 1:
                time.sleep(.5)
                x = input("Currency of the account: ")
                y = input("First Name: ")
                z = input("Last Name: ")
                savacc = BankAccount(x,y,z,"S")
                print("Congratulation ",y," ", z)
                print("You have opened a Savings Account")
                accdata.append([x,y,z,"S", BankAccount.handoff(savacc)])
                break
            elif mainM == 2:
                time.sleep(.5)
                time.sleep(.5)
                x = input("Currency of the account: ")
                y = input("First Name: ")
                z = input("Last Name: ")
                age = int(input("Age: "))
                savacc = BankAccount(x,y,z,"Y")
                if age > 26:
                    print("Sorry Youth Accounts are only aviable if you are 25 or less years old")
                    print("A savings account was automaticly created")
                else:
                    print("Congratulation ",y," ", z)
                    print("You have opened a Youth Account")
                accdata.append([x,y,z,"Y","0",age])
                break
            elif mainM == 3:
                print("Exiting current Menu")
                time.sleep(.5)
                break
            else:
                print("Input not recognised, try again")
    
    elif start == 3:
        print("Exiting")
        time.sleep(.5)
        break
    else:
        print("Input not recognised, try again")


    
#-----------------------------
#for n in SavingAccount.Withdraw(x,100):
#    print(n)
            
#class YouthAccount:
#    def __init__(self, currency, first , last):
#        self.first = first
#        self.last = last
#        self.balance = 0
#        self.currency = currency
#    def Deposit(self, amount):
#        if amount < self.balance:
#            return "invalid amount entered"
#        else:
#            self.balance = self.balance + amount
#            return self.balance
#    
#    def Withdraw(self, amount):
#        if amount > self.balance:
#            self.balance -= amount*1.02
#            return "Amount withdrawn ", amount,"New Balance ", self.balance
#        else:
#            self.balance -= amount
#            return "Amount withdrawn ", amount, "New Balance ", self.balance          
#    
#    def Interest(self, interest = 0.05):
#        self.balance = self.balance * (1+interest)
#        return self.balance
#    
#    def Owner(self):
#        return '{} {}'.format(self.first, self.last)
# 
#    def Currency(self):
#        return self.currency
#    
#    def Balance(self):
#        return self.balance  