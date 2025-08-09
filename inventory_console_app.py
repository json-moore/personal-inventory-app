# personal inventory console app

import json
import os

inventory = {}

# CRUD functions
def add_inventory():
    new_inventory = input('Please enter an item to add to iventory: ')
    item, quantity = new_inventory.split(',')
    inventory[item.strip()] = int(quantity.strip())
    print(inventory)
    return

def read_inventory():
    #stuff
    return #stuff

def edit_inventory():
    #insert
    return #stuff

def remove_inventory():
    #stuff
    return #stuff