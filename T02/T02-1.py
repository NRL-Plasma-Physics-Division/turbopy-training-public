class OrderClass:
    '''Superclass of the decorator classes'''
    def __init__(self, price=0, base='', size='', add_ins=[]):
        self.base = base
        self.size = size
        self.price = price
        self.add_ins = add_ins
    def cost(self):
        '''Returns a string representation of the price'''
        formated_price = str(self.price).ljust(4, '0')
        return f'${formated_price}'
    def description(self):
        '''Returns a string representation of the order'''
        if self.add_ins:
            formated_add_ins = ', '.join(self.add_ins)
            return f'{self.size} {self.base} with {formated_add_ins}'
        return f'{self.size} {self.base}'

class BaseClass(OrderClass):
    '''Decorates the order with the base drink'''
    def __init__(self, order, base):
        order.price += self.bases[base]
        super().__init__(order.price, base)
    bases = {'Coffee' : 2.50,
             'Espresso' : 1.50,
             'Black Tea' : 2.50,
             'Green Tea' : 2.75}

class SizeClass(OrderClass):
    '''Decorates the order with a size'''
    def __init__(self, order, size):
        order.price *= self.sizes[size]
        super().__init__(round(order.price, 2), order.base, size)
    sizes = {'Small' : 0.8,
             'Medium' : 1.0,
             'Large' : 1.4}

class AddInsClass(OrderClass):
    '''Decorates the order with add ins'''
    def __init__(self, order, add_in):
        order.price += self.add_ins[add_in]
        order.add_ins.append(add_in)
        super().__init__(order.price, order.base, order.size, order.add_ins)
    add_ins = {'2% Milk' : 0.50,
               'Soy Milk' : 0.50,
               'Almond Milk' : 0.50,
               'Ice' : 0.25,
               'Simple Syrup' : 0.25,
               'Caramel' : 0.50,
               'Boba' : 1.00,
               'Espresso Shot' : 1.50}

drink = OrderClass()
while 1:
    INPUT_BASE = str.title(input('Enter base drink: '))
    try:
        drink = BaseClass(drink, INPUT_BASE)
        break
    except KeyError:
        print('Please enter a valid base drink')
while 1:
    INPUT_SIZE = str.title(input('Enter size: '))
    try:
        drink = SizeClass(drink, INPUT_SIZE)
        break
    except KeyError:
        print('Please enter a valid size')
while 1:
    INPUT_ADD_IN = str.title(input('Enter add in (enter \'Done\' when finished): '))
    if INPUT_ADD_IN == 'Done':
        break
    if INPUT_ADD_IN in drink.add_ins:
        print('Cannot have more than one of each add in')
        continue
    try:
        drink = AddInsClass(drink, INPUT_ADD_IN)
    except KeyError:
        print('Please enter a valid add in')
print('')
print(drink.description())
print(drink.cost())
