# def drink(money): 
#     if money >= 2:
#         return "You've got yourself a soup!"
#     else:
#         return "No soup for you!"
    

# print(drink(4))
# print(drink(1))

def alcohol(age, money):
    if (age >= 21) and (money >= 5):
        return "We are getting a drink!"
    elif (age >= 21) and (money < 5):
        return "LOL you are not getting a drink, sorry!"
    elif (age < 21) and (money >= 5):
        return "Nice try kid!"
    else:
        return "You are too young and too poor"


# Optional: test with other examples
print(alcohol(21, 5))
print(alcohol(21, 3))
print(alcohol(18, 5))
print(alcohol(18, 2))
