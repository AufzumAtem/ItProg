# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 09:15:24 2017

@author: Romeo
"""

def print_numbers(x):
    for n in x:
        print(n,x[n])
def add_number(x):
    number = str(input("Input Number: "))
    name = str(input("Input full name: "))
    x.update({number: name})
def lookup_number(x):
    y = str(input("Name or Number: "))
    if y == 'Name':
        name = str(input("Enter Name: "))
        print(list(x.keys())[list(x.values()).index(name)])
    elif y == 'Number':
        number = str(input("Input Number: "))
        print(x[number])
def remove_number(x):
    y = str(input("Name or Number: "))
    if y == 'Name':
        name = str(input("Enter Name: "))
        number = list(x.keys())[list(x.values()).index(name)]
        x.pop(number, None)
    if y == 'Number':
        number = str(input("Input Number: "))
        x.pop(number, None)
def load_numbers(x):
    x = eval(open('Phonebook.txt').read())
    return x;
def save_numbers(x):
    f = open('Phonebook.txt', 'w' )
    f.write(str(x))
def print_menu():
    print('1. Print Phone Numbers')
    print('2. Add a Phone Number')
    print('3. Remove a Phone Number')
    print('4. Lookup a Phone Number')
    print('5. Load numbers')
    print('6. Save numbers')
    print('7. Quit')
    print
phone_book = {}
menu_choice = 0
print_menu()
while True:
    menu_choice = int(input("Type in a number (1-­‐7): "))
    if menu_choice == 1:
        print_numbers(phone_book)
    elif menu_choice == 2:
        print("Add Name and Number")
        add_number(phone_book)
    elif menu_choice == 3:
        print("Remove Name and Number")
        remove_number(phone_book)
    elif menu_choice == 4:
        print("Lookup Number")
        lookup_number(phone_book)
    elif menu_choice == 5:
        phone_book = load_numbers(phone_book)
    elif menu_choice == 6:
        save_numbers(phone_book)
    elif menu_choice == 7:
        break
    else:
        print_menu()