"""Solution to coffee shop problem"""


class Order:
    """
    The base order class

    Attributes
    ----------
    drink : str
        The drink as found in the Drinks dictionary

    """

    Extras = {"2% Milk": 0.50, "Soy Milk": 0.50,
              "Almond Milk": 0.50, "Ice": 0.25,
              "Simple Syrup": 0.25, "Caramel": 0.50,
              "Boba": 1.00, "Espresso Shot": 1.50}
    Drinks = {"Coffee": 2.50, "Espresso": 1.50,
              "Black Tea": 2.50, "Green Tea": 2.75}
    Sizecost = {"Small": 0.00, "Medium": 1.00, "Large": 2.00}

    def __init__(self, drink):
        """Initializes the base drink

        Parameters
        ---------
        str : drink
            String only found as a key in the Drinks dictionary

        """
        self.drink = drink

    def cost(self):
        """
        Returns the cost of the base drink

        Returns
        -------
        float
            The dictionary value for cost using the drink as key in Drinks

        """
        return Order.Drinks[self.drink]

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
            The added cost of the new size, as found in Sizecost
        """
        total = Order.Sizecost[self.size]
        total += Order.Drinks[self.drink]
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
        only extras found in the Extras dictionary are valid

    """

    def __init__(self, other_order, addons):
        """
        Initializes an Extra object, an Order object with a list of addons

        Parameters
        ----------
        other_order: Order
            Order object from which the base drink string is inherited
        addons : list
            List with strings for extras added, as found in Extras

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
        total = Order.Sizecost[self.size]
        total += Order.Drinks[self.drink]
        first = True
        for addon in self.addons:
            if first:
                first = False
                continue
            total += Order.Extras[addon]
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


if __name__ == "__main__":
    print("--------Menu--------\n\n"
          "Price of each drink\n"
          "~~~~~~~~~~~~~~~~~~~~")
    for index in Order.Drinks:
        print("${} {}".format(Order.Drinks[index], index))
    print("\nPrice increase with each size\n"
          "~~~~~~~~~~~~~~~~~~~~")
    for index in Order.Sizecost:
        print("${} {}".format(Order.Sizecost[index], index))
    print("\nPrice of each extra"
          "\nFirst extra is free"
          "\n~~~~~~~~~~~~~~~~~~~~")
    for index in Order.Extras:
        print("${} {}".format(Order.Extras[index], index))
    user_drink = input("Enter the drink: ")
    while user_drink not in Order.Drinks:
        user_drink = input("Please enter exactly as it appears: ")
    user_size = input("Enter the size: ")
    while user_size not in Order.Sizecost:
        user_size = input("Please enter exactly as it appears: ")
    user_extras = []
    user_input = input("Enter an extra to add it, or any character to order: ")
    while user_input in Order.Extras:
        user_extras.append(user_input)
        user_input = input("Enter an extra to add it, "
                           "or any character to order: ")
    final_order = Order(user_drink)
    final_size = Size(final_order, user_size)
    final_extras = Extra(final_size, user_extras)
    print("\n~~~~~~~~~~~~~~~~~~~~\n")
    print(f"{final_order.description()}{final_size.description()}", end="")
    print(f"{final_extras.description()}")
    print("Your order will cost ", end="")
    print(f"${final_extras.cost()}")
