class Base:
    drinks = {
        'coffee': 2.5,
        'espresso': 1.5,
        'black tea': 2.5,
        'green tea': 2.75
    }
    sizes = {
        'tall': 1,
        'grande': 1.4,
        'venti': 1.6
    }
    
    def __init__(self, drink, size):
        self.price = self.drinks[drink] * self.sizes[size]
        self.drink = drink
        self.size = size

    def cost(self):
        return '$%.2f' % self.price

    def description(self):
        return self.size + ' ' + self.drink


class AddOns(Base):
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
    
    def __init__(self, drink, addin, free):
        self._drink = drink
        self.addin = addin
        self._free = '(free)' if free else ''
        self.price = drink.price + self.addons[addin] if not free else drink.price
    
    def description(self):
        return f'{self._drink.description()} \n with {self.addin} {self._free}'
