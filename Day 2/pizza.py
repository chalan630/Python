'''
@Description: exp for Module
@Author: chalan630
@Date: 2019-12-27 09:12:25
@LastEditTime : 2020-02-08 15:22:34
'''
def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) + 
        "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
