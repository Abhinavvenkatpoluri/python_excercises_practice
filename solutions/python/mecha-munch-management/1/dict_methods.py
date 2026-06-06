"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
     for items in items_to_add:
         current_cart.setdefault(items,0)
         current_cart[items]+=1
     return current_cart       


def read_notes(notes):
  return dict.fromkeys(notes,1)


def update_recipes(ideas, recipe_updates):
    ideas.update(recipe_updates)
    return ideas


def sort_entries(cart):
   return dict(sorted(cart.items()))


def send_to_store(cart, aisle_mapping):
    new_dict = {}

    for key, quantity in cart.items():
        aisle, refrigerated = aisle_mapping[key]
        new_dict[key] = [quantity, aisle, refrigerated]

    return dict(sorted(new_dict.items(), reverse=True))
        

def update_store_inventory(fulfillment_cart, store_inventory):
    for key, value in store_inventory.items():
        if key in fulfillment_cart:
           ordered = fulfillment_cart[key][0]

           value[0] -= ordered

           if value[0] == 0:
              value[0] = "Out of Stock"

    return store_inventory
    
    
