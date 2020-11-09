"""
My solution to the coffeeshop problem posed for 02, Object Oriented Python

Edited and improved in T03, test-driven-development.
"""
class Order:
    """
    Base order class, doesn't feature any add-ins

    Parameters
    ----------
    base : str
        Base drink, to be stored in `base`, default value of "Coffee"
    size : str
        Drink size, to be stored in `size`, default value of "Small"

    Attributes
    ----------
    baseMenu : dict
        Dictionary with names of drinks as keys and prices as values
    sizes : dict
        Dictionary with sizes as keys and price multipliers as values
    addOnsMenu : dict
        Dictionary with add-in names as keys and prices as values
    fullMenu : dict
        Dictionary combining `baseMenu` and `addOnsMenu`
    base : str
        Name of the drink, must be a key in `baseMenu`
    size : str
        Size of the base drink, must be a key in `sizes`
    """
    baseMenu = {
                "Coffee": 2.50,
                "Espresso": 1.50,
                "Black Tea": 2.50,
                "Green Tea": 2.75}
    sizes = {
                "Small": 1.00,
                "Medium": 1.50,
                "Large": 1.60}
    addOnsMenu = {
                "2% milk": .50,
                "Soy milk": .50,
                "Almond milk": .50,
                "Ice": .25,
                "Simple syrup": .25,
                "Caramel": .50,
                "Boba": 1.00,
                "Espresso Shot": 1.50}

    fullMenu = {**baseMenu, **addOnsMenu}

    def __init__(self, base="Coffee", size="Small"):
        """Initializes with type of drink (can be base drink or add-on) and an optional size."""
        self.base = base
        self.size = size

    def cost(self):
        """
        Returns the base cost of an order

        Returns
        -------
        float
            Cost of the drink.
            Calculated by multiplying the value in `fullMenu` by the value in `sizes`
        """
        cost = Order.fullMenu[self.base]*Order.sizes[self.size]
        return  cost

    def __str__(self):
        """Overrides default __str__ method to redefine the description of an order"""
        order = "Your order is a "
        order += self.size + " "
        order += self.base
        return order

    def description(self):
        """
        Returns the string representation of an order in a human-readable fashion

        Returns
        -------
        str
            The size and name of the order appended to 'Your order is a'
        """
        return str(self)

class AddIn(Order):
    """
    Subclass of Order used to add add-ins from the add-in menu

    Parameters
    ----------
    order : Order
        The base order being added onto, stored in `order`
    add_on : str
        The add-in being added in, stored in `add-in`

    Attributes
    ----------
    order : Order
        Base order that is being added onto
    add_on : str
        An add-in, must correspond to a key in `addOnsMenu`
    """
    def __init__(self, order, add_on):
        """Initializer with an Order object and a new add-in"""
        self.order = order
        self.add_on = add_on

    def cost(self):
        """
        Adds cost of the add-in to the cost of the drink so far

        Calls the cost of `order` and adds the cost of `add_on`.
        Notably, the cost of the first add-in isn't added.

        Returns
        -------
        float
            The cost of the drink including the new add-in
        """
        cost = self.order.cost()
        if isinstance(self.order, AddIn):  #True for all but the first add-in
            cost += Order.addOnsMenu[self.add_on]
        return cost

    def description(self):
        """
        Adds the new add-in to the description of the drink in a human-readable way


        If it's the first add-in, it formats the description to fit.
        The final string should contain the base order description, `add_on`, and "with"

        Returns
        -------
        str
            The description of the drink with add-in
        """
        des = self.order.description()
        if "with" not in des:
            des += " with "
        des += self.add_on + ", "
        return des
