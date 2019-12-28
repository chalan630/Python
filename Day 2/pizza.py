'''
@Descripttion: exp for Module
@version: 
@Author: chalan630
@Date: 2019-12-27 09:12:25
@LastEditTime : 2019-12-27 09:14:57
'''
def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) + 
        "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
