# personal inventory console app

import json
import os
import time

inventory = {}

def main_menu():
    #stuff
    return

# CRUD functions
def add_inventory():

    last_entry = None
    print('[ ADDING Inventory . . . ]\n')

    while True:
        new_inventory = input('To add inventory, enter item and quantity as formatted below.\n'
                              '(Enter x to stop adding inventory)\n'
                              '(Enter r to remove the last recent entry)\n\n'
                              '[item name], [quantity]: ').lower()
        
        if new_inventory == 'x':
            break
        if new_inventory == 'r':
            if last_entry in inventory:
                inventory.pop(last_entry)
                print(f'Removed: [{last_entry}, Qty: {last_quantity}]\n')
                time.sleep(1)
                continue
            elif last_entry not in inventory:
                print('No recent entries found.\n')
                time.sleep(1)
                continue

        try:
            item, quantity = new_inventory.split(',')
            quantity = int(quantity.strip())
            inventory[item.strip()] = quantity
            print(f'Added: [{item.strip()}, Qty: {quantity}]\n')
            time.sleep(1)
            last_entry = item
            last_quantity = quantity
            continue
        except ValueError:
            print('Please enter a valid quantity.\n')
            time.sleep(1)
            continue
    return inventory

def read_inventory():
    print(inventory)
    # add a way to search the inventory
    return #stuff

def edit_inventory():
    #insert
    return #stuff

def remove_inventory():
    #stuff
    return #stuff