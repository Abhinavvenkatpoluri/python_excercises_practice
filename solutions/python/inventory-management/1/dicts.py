"""Functions to keep track and alter inventory."""


def create_inventory(items):
   inventory={}
   for item in items:
        inventory[item] = inventory.get(item,0) + 1
   return inventory


def add_items(inventory, items):
    for item in items:
        inventory[item] = inventory.get(item,0) + 1
    return inventory


def decrement_items(inventory, items):
    for item in items:
        if inventory.get(item, 0) > 0:
            inventory[item] -= 1
    return inventory


def remove_item(inventory, item):
    if item in inventory:
       inventory.pop(item)
    return inventory      


def list_inventory(inventory):
    new_list=[]
    for item,value in inventory.items():
        if value>0:
           new_list.append((item,value))

    return new_list
