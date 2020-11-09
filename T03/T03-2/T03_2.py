'''Setup for taking an order according to the coffee-shop problem'''
class Drink:
    '''Class stores all values and methods for the order'''
    def __init__(self, base, size, price):
        '''Creates drink with a base drink, a size, and a base price'''
        self.base = base
        self.size = size
        self.price = price
        self.add_ins = []
    def cost(self):
        '''Returns a formated string showing the total cost of the drink'''
        if self.add_ins: # Removes the price of the first add in if the drink has add ins
            formated_price = str(self.price - ADD_INS[self.add_ins[0]]).ljust(4, '0')
        else: # Otherwise, if there are no add ins, just return the normal price
            formated_price = str(self.price).ljust(4, '0')
        return f'${formated_price}'
    def description(self):
        '''Returns a formated string that lists the size, base drink, and add ins'''
        if self.add_ins: # Returns the 'with' and list of add ins only if there are add ins
            formated_order = ', '.join(self.add_ins)
            return f'{self.size} {self.base} with {formated_order}'
        return f'{self.size} {self.base}'
    def add(self, add_in):
        '''Adds an add in to the drink and adds the price to the total'''
        self.add_ins.append(add_in)
        self.price += ADD_INS[add_in]
# Dictionary of base drinks and their base prices
BASES = {'Coffee' : 2.50,
         'Espresso' : 1.50,
         'Black Tea' : 2.50,
         'Green Tea' : 2.75}

# Dictionary of sizes, numbers act as multipliers for the base price
SIZES = {'Small' : 0.8,
         'Medium' : 1.0,
         'Large' : 1.4}

# Dictionary of add ins and their prices
ADD_INS = {'2% Milk' : 0.50,
           'Soy Milk' : 0.50,
           'Almond Milk' : 0.50,
           'Ice' : 0.25,
           'Simple Syrup' : 0.25,
           'Caramel' : 0.50,
           'Boba' : 1.00,
           'Espresso Shot' : 1.50}
           
