class beverage:
    """
    A class representing a basic drink

    Parameters
    ----------
    drink : str
        Type of base drink
    size : str
        Size of drink

    Attributes
    ----------
    drink : str
        Type of base drink
    size : str
        Size of drink
    cost : float
        Price of drink
    drinks : dict (str : float)
        Drink names with corresponding base price
    sizes : dict (str : float)
        Drink sizes with corresponding price multiplier
    """
    drinks = {'coffee': 2.5,
              'espresso': 1.5,
              'black tea': 2.5,
              'green tea': 2.75}
    sizes = {'s': 0.8, 'm': 1, 'l': 1.2}

    def __init__(self, drink, size):
        self.drink = drink
        self.size = size
        self.cost = self.drinks[drink] * self.sizes[size]


class drink_with_toppings(beverage):
    """
    A class representing a drink with toppings

    Parameters
    ----------
    bev : beverage
        Type of base beverage
    additions : list of strings
        Toppings of new beverage

    Attributes
    ----------
    additions : list of strings
        Toppings of new beverage
    cost : float
        Price of drink
    toppings : dict (str : float)
        Topping names with corresponding price
    """
    toppings = {'2% milk': 0.5,
                'soy milk': 0.5,
                'almond milk': 0.5,
                'ice': 0.25,
                'simple syrup': 0.25,
                'caramel': 0.5,
                'boba': 1,
                'espresso shot': 1.5}

    def __init__(self, bev, additions):
        super().__init__(bev.drink, bev.size)
        self.additions = additions
        self.cost += sum([self.toppings[add] for add in self.additions]) # add all toppings
        self.cost -= self.toppings[self.additions[0]] # take out the first topping

MY_ORDER = drink_with_toppings(beverage('green tea', 's'), ['soy milk', 'ice', 'caramel', 'boba'])
print('$' + str(MY_ORDER.cost))
