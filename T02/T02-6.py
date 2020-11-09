"""Takes users drink order from menu, printing the description and cost."""


class Base:
    """
    A class used to represent drink bases.
    
    Parameters
    ----------
    drink : str
        The type of drink for base, must be key in drinks dictionary
    size : str
        The size of drink, must be key in sizes dictionary

    Attributes
    ----------
    price : float
        Price of drink for specific size and base
    drink : str
        The base drink, a key in drinks dictionary
    size : str
        The size of the drink, a key in the sizes dictionary
    """
    
    drinks = {
        'coffee': 2.5,
        'espresso': 1.5,
        'black tea': 2.5,
        'green tea': 2.75
    }
    """Base drink options and their costs (`dict`).
    """
    
    sizes = {
        'tall': 1,
        'grande': 1.4,
        'venti': 1.6
    }
    """Different sizes of drinks and the factor by which the base cost will be multiplied (`dict`).
    """
    
    def __init__(self, drink, size):
        self.price = self.drinks[drink] * self.sizes[size]
        self.drink = drink
        self.size = size
    
    def cost(self):
        """
        Returns a formmated cost of the drink

        Returns
        -------
        str
            Formatted price string
        """
        return '$%.2f' % self.price
    
    def description(self):
        """
        Returns a description of the drink

        Returns
        -------
        str
            String of the size and type of drink
        """
        return self.size + ' ' + self.drink


class AddOns(Base):
    """
    A decorator and sub class of base for any addons to the base drink.

    Parameters
    ----------
    drink : :class: `Base`
        The drink you are adding an addon to
    addin : str
        The addon you are adding to your drink, must be key in addons dictionary
    free : bool
        Whether or not the addin is free

    Attributes
    ----------
    addin : str
        Type of addon to the drink, a key in the addons dictionary
    price : float
        Total price of the drink with the addon if the addon is not free
    """
    addons = {
        'soy milk': 0.5,
        'almond milk': 0.5,
        '2% milk': 0.5,
        'caramel': 0.5,
        'simple syrup': 0.25,
        'ice': 0.25,
        'boba': 1,
        'espresso shot': 1.5
    }
    """Drink addon options and their prices (`dict`).
    """
    
    def __init__(self, drink, addin, free):
        self._drink = drink
        self.addin = addin
        self._free = '(free)' if free else ''
        self.price = drink.price + self.addons[addin] if not free else drink.price
    
    def description(self):
        """
        Returns a description of the drink with the addons

        Returns
        -------
        str
            Formatted string of the drinks description with each addon and whether it was free
        """
        return f'{self._drink.description()} \n with {self.addin} {self._free}'


if __name__ == '__main__':
    
    print('drinks menu:\n' + '\n'.join([f'{a:16}... $%.2f' % Base.drinks[a] for a in Base.drinks]))
    
    order = input('drink order: ').strip()
    while order.lower() not in Base.drinks:
        order = input('please choose valid drink: ').strip()
    
    print('\nsizes:\n' + '\n'.join([f'{a:8}\t... $%.2f' % (Base.sizes[a] * Base.drinks[order]) for a in Base.sizes]))
    
    size = input('size: ').strip()
    while size.lower() not in Base.sizes:
        size = input('please choose valid size: ').strip()
    order = Base(order.lower(), size.lower())
    
    print('\naddins: \n' + '\n'.join([f'{a.replace("%", "%%"):24}... $%.2f' % AddOns.addons[a] for a in AddOns.addons]))
    
    count = 1
    print('first addin free!')
    while True:
        addin = input('addin %d: ' % count).lower().strip()
        if not addin: break
        while addin not in AddOns.addons:
            addin = input('please choose valid addin: ').lower().strip()
            if not addin: break
        else:
            order = AddOns(order, addin, True) if count == 1 else AddOns(order, addin, False)
            count += 1
            continue
        break
    
    print('\nyour order: \n' + order.description())
    print('price: %s' % order.cost())
