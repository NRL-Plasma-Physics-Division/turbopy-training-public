"""Coffee House Problem"""

"""For some reason I wasn't get the dictionaries to work in the classes.
Probably just something weird since others have gotten it to work fine."""

######## Global Dictionaries ########
menu_items = {'Coffee': 2.50,
              'Espresso': 1.50,
              'Black Tea': 2.50,
              'Green Tea': 2.75
              }

addin_items = {'2% Milk': 0.50,
               'Soy Milk': 0.50,
               'Almond Milk': 0.50,
               'Ice': 0.25,
               'Simply Syrup': 0.25,
               'Caramel': 0.50,
               'Boba': 1.00,
               'Espresso Shot': 1.50
              }

drink_size = {'Small': -0.50,
              'Medium': 0.0,
              'Large': 0.50
              }

restuarant_items = {**menu_items, **addin_items, **drink_size}


######## Classes ########
class Menu:
    """initial base class - Menu"""
    def __init__(self, order): # order = main menu item
        """initializer"""
        self._description = order 
        self._cost = restuarant_items[order] # gets the cost from the total item dictionary 
        
    def description(self):
        """return description of order"""
        return self._description
    
    def cost(self):
        """return cost of order"""
        return self._cost
    
class AddIn(Menu):
    """Child class of Menu"""
    def __init__(self, wrap_prev, order):
        """will wrap previous order"""
        super().__init__(order) # grab the __init__ self._description and self._cost from Menu
        self._wrap = wrap_prev
        
    def description(self):
        """return description of the menu + addin order"""
        return ' with '.join([self._wrap.description(), self._description]) # _wrap.description() returns str
    
    def cost(self):
        """return cost of menu + addin order"""
        return self._wrap.cost() + self._cost # _wrap.cost() returns float of previous order cost
    
class DrinkSize(AddIn):
    """Child class of Addin"""
    def __init__(self, wrap_prev, order): # wrap_prev = addin totals, order = size input
        """will wrap previous order and add the size"""
        super().__init__(wrap_prev, order) # need both the previous order and the current order
        self._wrap = wrap_prev
        
    def description(self):
        """returns description of the menu + addin + drink size"""
        return 'A {} {}'.format(self._description, self._wrap.description())
    
    def cost(self):
        """returns cost of menu + addin + drink size"""
        return self._wrap.cost() + self._cost
    

########### Welcome Message ###########
print('Welcome to Turbo Coffee House!\n')

print('****Our Menu****')
for key, val in menu_items.items():
    print(f'{key}: ${val:.2f}')

print('\n****Our Addins****')
for key, val in addin_items.items():
    print(f'{key}: ${val:.2f}')
print('*Your least valued addin is free!*')

print('\n****Sizes****')
for key, val in drink_size.items():
    print(f'{key}: ${val:.2f}')
print('*************\n')
    
####### Main Code #######
"""Menu input"""
menu_input = input('What would you like to order? ')
while menu_items.get(menu_input) == None: # checks for incorrect input
    menu_input = input("I'm sorry, what would you like? ")

persons_order = Menu(menu_input) # initializing the order

"""Addin inputs"""
addin_input = input('What would you like to add to that? ("Nothing" to finish) ') # first addin
if addin_input == str('Nothing'):
    addin_min_price = 0
else:
    addin_min_price = None # initial minimum addin price
while addin_input != str('Nothing'):
    while addin_items.get(addin_input) == None: # checks for user exit
        addin_input = input("I'm sorry, what would you like? ")
        if addin_input == str('Nothing'): 
            addin_min_price = 0 # sets the minimum addin price
            break # exits the loop
    
    # establishing the minimum addin price
    if addin_min_price == None: # if the initial input is in the addin_items dictionary
        addin_min_price = addin_items[addin_input] # make it the new min price
    elif addin_input == str('Nothing'):
        break  # exits the loop before key value error
    elif addin_items[addin_input] < addin_min_price: # if the next addin item costs less than the previous,
        addin_min_price = addin_items[addin_input] # make it the new min price
        
    persons_order = AddIn(persons_order, addin_input) # adding the addins to the order
    
    addin_input = input('What would you like to add to that? ("Nothing" to finish) ') # next addin, starts loop over

"""Size input"""    
size_input = input('What size would you like? ')
while drink_size.get(size_input) == None:
    size_input = input("I'm sorry, what size? ")

persons_order = DrinkSize(persons_order, size_input) # adding the drinks to the order


####### Show final order #######
print('\nYour order is: {}'.format(persons_order.description()))
print('Your order cost is: ${:.2f}'.format(persons_order.cost() - addin_min_price)) # notice we remove the minimum addin cost
print('Thank you, please come again!')
