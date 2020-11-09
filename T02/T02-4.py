"""My solution to the coffeeshop problem posed for 02, Object Oriented Python"""

class Order:
    """
    Base order class, doesn't feature any add-ins

    Parameters
    ----------
    base : str
        To be stored in `self.base`
    size : str
        To be stored in `self.size`, defaults to "Small"

    Attributes
    ---------
    baseMenu : dict
        Dictionary associating names and prices of base orders
    sizes : dict
        Dictionary associating names and cost multipliers of order sizes
    addOnsMenu : dict
        Dictionary associating names and costs of add-ins
    fullMenu : dict
        Dictionary combining `baseMenu` and `addOnsMenu`
    base : str
        Base type of drink, corresponds to a key in `baseMenu`
    size : str
        Size of drink, corresponds to a key in `sizes`
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


    def __init__(self, base, size="Small"):
        """Initializes with type of drink (can be base drink or add-on) and an optional size."""
        self.base = base
        self.size = size


    def cost(self):
        """
        Returns the base cost of an order

        Returns
        -------
        float
            Drink size multiplied by drink cost,
            both accessed by plugging relevant attributes into relevant menus
        """
        cost = Order.fullMenu[self.base]
        cost *= Order.sizes[self.size]
        return  cost


    def __str__(self):
        """Overrides default __str__ method to redefine the description of an order"""
        order = "Your order is a "
        order += self.size + " "
        order += self.base
        return order


    def description(self):
        """
        Returns the string representation of the order as defined in __str__

        Returns
        -------
        str
            Formatted string containing the size and type of drink
        """
        return str(self)

class AddIn(Order):
    """
    Subclass of Order used to add add-ins from the add-in menu

    Parameters
    ----------
    order : Order
        To be plugged into `self.order`
    add_on : str
        To be plugged into `self.add_on`

    Attributes
    ----------
    order : Order
        Order being added onto
    add_on : str
        Add-in, corresponds to a value in `Order.addOnsMenu`
    """


    def __init__(self, order, add_on):
        """Initializer with an Order object and a new add-in"""
        self.order = order
        self.add_on = add_on


    def cost(self):
        """
        Adds cost of the add-in to the cost of the drink so far. The first add-in is free.

        Returns
        -------
        float
            Value corresponding to `add_on` in the menu plus the cost of `order`
        """
        cost = self.order.cost()
        if isinstance(self.order, AddIn):  #True for all but the first add-in
            cost += Order.addOnsMenu[self.add_on]
        return cost


    def description(self):
        """
        Adds the new add-in to the description of the drink.

        Returns
        -------
        str
            Appends `add_on` to the description of `order`
            If it's the first add-in, it formats the string to match
        """
        des = self.order.description()
        if "with" not in des:
            des += " with "
        des += self.add_on + ", "
        return des


MAIN_MENU = ""
for item in Order.baseMenu:
    MAIN_MENU += item + "\n"
print(f"Menu:\n{MAIN_MENU}")

DRINK_TYPE = input("What would you like as your base order? ")
DRINK_SIZE = input("What size (Small, Medium, Large)? ")

NEW_ORDER = Order(DRINK_TYPE, DRINK_SIZE)

ADD_ON_MENU = ""
for item in Order.addOnsMenu:
    ADD_ON_MENU += item + "\n"
print(f"\nAdd-ins:\n{ADD_ON_MENU}")


while True:
    PROMPT = "If you would like an add-in, enter it here."
    PROMPT += " The first one's free! If not, just hit enter. "
    ADD_ON = input(PROMPT)
    if not ADD_ON:
        break
    NEW_ORDER = AddIn(NEW_ORDER, ADD_ON)

print(NEW_ORDER.description())
print("That will be $%.2f" % NEW_ORDER.cost())
