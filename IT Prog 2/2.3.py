# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 13:14:00 2018

@author: Romeo
"""

class bankaccount:
    def __init__(self, currency, first , last):
        self.first = first
        self.last = last
        self.balance = 0
        self.currency = currency
        
    def deposit(self, amount):
        if amount < self.balance:
            return "invalid amount entered"
        else:
            self.balance = self.balance + amount
            return self.balance
    def withdraw(self, amount):
        if amount > self.balance:
            return "invalid amount entered"
        else:
            self.balance = self.balance - amount
            return self.balance            
    def owner(self):
        return '{} {}'.format(self.first, self.last), self.balance
    def currency(self):
        return self.currency
    def balance(self):
        return self.balance
    
acc1 = bankaccount("USD","Romeo", "Moritzi")
acc2 = bankaccount("CHF","Test", "User")
print(bankaccount.balance(acc1))
print(bankaccount.deposit(acc1,1000))
print(bankaccount.withdraw(acc1, 1200))
print(bankaccount.balance(acc1))
print(bankaccount.withdraw(acc1, 200))
print(bankaccount.balance(acc1))
print(bankaccount.currency(acc1))
print(bankaccount.currency(acc2))
print(bankaccount.owner(acc1))
print(bankaccount.owner(acc2))