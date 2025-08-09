# personal inventory console app

import json
import os
import time

inventory = {}

# CRUD functions
def add_inventory():
    while True:
        new_inventory = input('To add inventory, enter item and quantity as formatted below. (Enter x to stop adding inventory)\n'
                            '[item name], [quantity]: ')
        last_entry = (item.strip(), int(quantity.strip()))
        if new_inventory == 'x':
            break

        # add statement to remove last entry into dictionary - incomplete
        if new_inventory =='r':
            inventory.pop(last_entry, None)
        # remove last entry -- end

        try:
            item, quantity = new_inventory.split(',')
            inventory[item.strip()] = int(quantity.strip())
            print(f'\nAdded: {item.strip()}, Quantity: {quantity.strip()}')
            print(inventory)
            continue
        except ValueError:
            print('\nPlease enter a valid quantity.\n')
    return inventory

def read_inventory():
    #stuff
    return #stuff

def edit_inventory():
    #insert
    return #stuff

def remove_inventory():
    #stuff
    return #stuff