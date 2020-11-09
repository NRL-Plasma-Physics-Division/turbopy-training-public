class beverage:
    drinks = {'coffee': 2.5, 'espresso': 1.5, 'black tea': 2.5, 'green tea': 2.75}
    sizes = {'s': 0.8, 'm': 1, 'l': 1.2}
    def __init__(self, drink, size):
        self.drink = drink
        self.size = size
        self.cost = self.drinks[drink] * self.sizes[size]


class topping(beverage):
    toppings = {'2% milk': 0.5,'soy milk': 0.5, 'almond milk': 0.5,'ice': 0.25,'simple syrup': 0.25, 'caramel': 0.5,'boba': 1,'espresso shot': 1.5}
    def __init__(self, drink, additions):
        self._drink = drink
        self.additions = additions
        self.cost = drink.cost
        first_topping = True
        for add in additions:
            if first_topping:
                first_topping = False
                continue
            self.cost+=self.toppings[add]


my_order = topping(beverage('green tea', 's'), ['soy milk', 'ice', 'caramel', 'boba'])
print('$' + str(my_order.cost))
