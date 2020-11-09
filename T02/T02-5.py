"""
Example problem. Use the decorator pattern to make a "menu" for a coffee shop.
"""

base_menu = {
    "coffee": 2.5,
    "espresso": 1.5,
    "black tea": 2.5,
    "green tea": 2.5,
}

addin_menu = {
    "2% milk": 0.5,
    "soy milk": 0.5,
    "almond milk": 0.5,
    "ice": 0.25,
    "simple syrup": 0.5,
    "caramel": 0.5,
    "boba": 0.5,
    "espresso shot": 1.5,
}

full_menu = {**base_menu, **addin_menu}

class MenuItem:
    """Base class for any menu item"""
    def __init__(self, description):
        """Initialize"""
        self._description = description
        self._cost = full_menu[description]

    def cost(self):
        """Return cost of this item"""
        return self._cost

    def description(self):
        """Return a string with the description of this item"""
        return self._description


class AddIn(MenuItem):
    """Derived class that can be used to decorate a MenuItem"""
    def __init__(self, wrapped, description):
        super().__init__(description)
        self._wrapped = wrapped

    def cost(self):
        """Return cost of this item"""
        return self._cost + self._wrapped.cost()

    def description(self):
        """Return a string with the description of this item"""
        return " with ".join([self._wrapped.description(), self._description]).strip()


if __name__ == "__main__":
    # "Run" the coffee shop example

    print()
    print('Welcome to "The Decorated Café"!')
    print()

    menusize = max([len(k) for k in full_menu]) + 4

    print("This is the menu:")
    for k, v in base_menu.items():
        print(f"{k:>{menusize}}: ${v:.02f}")

    print("And these are the add-ins you can get:")
    for k, v in addin_menu.items():
        print(f"{k:>{menusize}}: ${v:.02f}")

    # Order iced soy coffee
    order = MenuItem("coffee")
    order = AddIn(order, "soy milk")
    order = AddIn(order, "ice")
    print()
    print(f"I'd like a {order.description()}, please.")
    print(f"Here's your {order.description()}. That will be ${order.cost():.02f}, please.")
