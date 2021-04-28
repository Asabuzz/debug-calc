#import numpy as np

def ask_user(sentence): # do_something OK
    choice = input(f"""{sentence}\n>""")
    return (choice)

def values(number):
    list_numbers = []
    while number.isdigit():
        list_numbers.append(int(number))
        number = ask_user("Saisir un chiffre à additionner ou clicker sur '=' ")
    return list_numbers

def addition(list_numbers): # do_something OK
    result = sum(list_numbers) # do_something OK
    return result

def multplication(list_numbers):    
    # #### REFACTORISATION NUMPY // Remplace toute la boucle for #####
    # result = np.prod(list_numbers) 
    for index, list_number in enumerate(list_numbers): # refactoriser OK
        if index == 0:
            result = list_number
        else:
            result *= list_number # do_something OK
    return result

def division(list_numbers):
    for index, list_number in enumerate(list_numbers): # refactoriser OK
        if index == 0:
            result = list_number
        else:
            result /= list_number # do_something OK
    return result

def soustraction(list_numbers):
    i = 0
    for list_number in list_numbers:
        if i == 0:
            result = list_number
        else:
            result -= list_number
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
        if choice < 5 :
            if choice == 1:
                number = ask_user("Saisir un chiffre à ADDITIONNER ou clicker sur '=' ")
                list_numbers = values(number)
                result = addition(list_numbers)
            elif choice == 2:
                number = ask_user("Saisir un chiffre à SOUSTRAIRE ou clicker sur '=' ")
                list_numbers = values(number)
                result = soustraction(list_numbers)
            elif choice == 3:
                number = ask_user("Saisir un chiffre à MULTIPLIER ou clicker sur '=' ")
                list_numbers = values(number)
                result = multplication(list_numbers)
            elif choice == 4:
                number = ask_user("Saisir un chiffre à DIVISER ou clicker sur '=' ")
                list_numbers = values(number)
                result = division(list_numbers)
            message = f"Le resultat est ==> {result}"
        else:
            message = "A bientôt !"
        
        return print(message)