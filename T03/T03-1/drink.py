"""Solution to coffee shop problem, modified for the pytest"""


class Order:
    """
    The base order class

    Attributes
    ----------
    drink : str
        The drink as found in the drinks dictionary

    """

    extras = {"2% Milk": 0.50, "Soy Milk": 0.50,
              "Almond Milk": 0.50, "Ice": 0.25,
              "Simple Syrup": 0.25, "Caramel": 0.50,
              "Boba": 1.00, "Espresso Shot": 1.50}
    drinks = {"Coffee": 2.50, "Espresso": 1.50,
              "Black Tea": 2.50, "Green Tea": 2.75}
    sizecost = {"Small": 0.00, "Medium": 1.00, "Large": 2.00}

    def __init__(self, drink):
        """Initializes the base drink

        Parameters
        ---------
        str : drink
            String only found as a key in the drinks dictionary

        """
        self.drink = drink

    def cost(self):
        """
        Returns the cost of the base drink

        Returns
        -------
        float
            The dictionary value for cost using the drink as key in drinks

        """
        return Order.drinks[self.drink]

    def description(self):
        """
        Returns a string describing the base order

        Returns
        -------
        str
            String describing the drink ordered

        """
        return f"Your order is a {self.drink}"


class Size(Order):
    """
    The class used to store the size addition to a base drink

    Attributes
    ----------
    str : size
        A string representing the size addition onto a base order
    drink : str
        A string representing the base drink from the modified order

    """

    def __init__(self, other_order, size):
        """
        Initializes an order as a new size object

        Parameters
        ----------
        other_order : Order
            Used to add size to the base drink from another order
        size : str
            A string representing the new size

        """
        super().__init__(self)
        self.size = size
        self.drink = other_order.drink

    def cost(self):
        """
        Calclates the added cost of the size addition

        Returns
        -------
        float
            The added cost of the new size, as found in sizecost
        """
        total = Order.sizecost[self.size]
        total += Order.drinks[self.drink]
        return total

    def description(self):
        """
        Adds a description about the size of a Size object

        Returns
        -------
        str
            A size-specific string to be added to the base drink description

        """
        return f", size {self.size},"


class Extra(Order):
    """
    Class that extends order to store a list of extras

    Attributes
    ----------
    drink : str
        String representing the base drink, taken from a base order object
    addons : list
        List containing any extras as strings added to the Order object,
        only extras found in the extras dictionary are valid

    """

    def __init__(self, other_order, addons):
        """
        Initializes an Extra object, an Order object with a list of addons

        Parameters
        ----------
        other_order: Order
            Order object from which the base drink string is inherited
        addons : list
            List with strings for extras added, as found in extras

        """
        super().__init__(self)
        self.drink = other_order.drink
        self.addons = addons
        self.size = other_order.size

    def cost(self):
        """
        Calculates the sum of the costs of each extra, the first being free

        Returns
        -------
        float
            Sum cost of the extras, first extra added is free

        """
        total = Order.sizecost[self.size]
        total += Order.drinks[self.drink]
        first = True
        for addon in self.addons:
            if first:
                first = False
                continue
            total += Order.extras[addon]
        return total

    def description(self):
        """
        Creates a string repesentation of the list of extras

        Returns
        -------
        str
            String with line breaks including extras listed in order

        """
        out = " with the following extras: "
        if not self.addons:
            return out + "\nNone"
        for addon in self.addons:
            out += f"\n - {addon}"
        return out
