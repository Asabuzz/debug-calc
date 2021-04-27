# import numpy as np

def ask_user(sentence): # do_something OK
    choice = input(f"""{sentence}\n>""")
    return (choice)

def addition(number): # do_something OK
    list_numbers = []
    while number.isdigit():
        if number.isdigit():
            list_numbers.append(int(number))
        number = ask_user("Saisir un chiffre à additionner ou cliquer sur '=' ")
    result = sum(list_numbers) # do_something OK
    return result

def multiplication(number):
    list_numbers = []
    while number.isdigit():
        if number.isdigit():
            list_numbers.append(int(number)) # do_something OK
        number = ask_user("Saisir un chiffre à multiplier ou cliquer sur '=' ")
        
    #result = np.prod(np.array(list_numbers)) #Refactorisation avec numpy
    
    # for list_number, index in zip(list_numbers,list(range(len(list_numbers)))): # refactoriser
    for index, list_number in enumerate(list_numbers):

        if index == 0: # do_something OK
            result = list_number
        else:
            result *= list_number # do_something Ok
    return result

def division(number):
    list_numbers = []
    while number.isdigit():
        if number.isdigit():
            list_numbers.append(int(number)) # do_something OK
        number = ask_user("Saisir un chiffre à diviser ou cliquer sur '=' ")
        
    # for list_number, index in zip(list_numbers,list(range(len(list_numbers)))): # refactoriser
    for index, list_number in enumerate(list_numbers):

        if index == 0:
            result = list_number
        else:
            result /= list_number # do_something OK
    return result

def soustraction(number):
    list_numbers = []
    while number.isdigit(): # do_something OK
        if number.isdigit():
            list_numbers.append(int(number)) # do_something OK
        number = ask_user("Saisir un chiffre à soustraire ou cliquer sur '=' ")
    i = 0
    for list_number in list_numbers:
        if i == 0:
            result = list_number
        else:
            result = result - list_number
        i = i + 1
    return result

def display_interface():
    choice = ask_user("""
    Tu veux :
    1. Additionner Tape 1
    2. Soustraire Tape 2
    3. Multiplier Tape 3
    4. Diviser Tape 4""")
    while choice.isdigit():
        choice = int(choice) # do_something OK
        if choice == 1:
            choice = ask_user("Saisir un chiffre à ADDITIONNER ou cliquer sur '=' ")
            result = addition(choice)
        elif choice == 2:
            choice = ask_user("Saisir un chiffre à SOUSTRAIRE ou cliquer sur '=' ")
            result = soustraction(choice)
        elif choice == 3:
            choice = ask_user("Saisir un chiffre à MULTIPLIER ou cliquer sur '=' ")
            result = multiplication(choice)
        elif choice == 4:
            choice = ask_user("Saisir un chiffre à DIVISER ou cliquer sur '=' ")
            result = division(choice)
        return print(f"Le resultat est ==> {result}")