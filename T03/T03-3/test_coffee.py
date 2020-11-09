"""Tests the classes from the coffeeshop program"""
from coffeeshop import Order, AddIn


def test_constructor():
    """Tests the Order constructor, both for default values, inputted values, and menus."""
    o = Order()

    assert o.base == "Coffee"
    assert o.size == "Small"

    o = Order("Espresso", "Medium")

    assert o.base == "Espresso"
    assert o.size == "Medium"
    assert isinstance(Order.sizes, dict)


def test_cost():
    """Tests that the cost method returns the right amount for base orders."""
    o = Order()
    assert o.cost() == 2.5
    o = Order(size="Large")
    assert o.cost() == 4


def test_description():
    """Tests that the description method returns a string with the proper components"""
    o = Order()

    assert isinstance(o.description(), str)
    assert o.base in o.description()
    assert o.size in o.description()


def test_add_init():
    """Tests the initializer for an add-in"""
    o = Order()
    a = AddIn(o, "Ice")

    assert a.order == o
    assert a.add_on == "Ice"


def test_add_cost():
    """Tests the cost for an add-in, factoring in the free first add-in"""
    a = AddIn(Order(), "Ice")
    b = AddIn(a, "Caramel")
    c = AddIn(b, "Boba")

    assert a.cost() == 2.5
    assert b.cost() == 3
    assert c.cost() == 4


def test_add_description():
    """Tests that the add-in description function contains each of the add-ins added"""
    a = AddIn(Order(), "Ice")
    a = AddIn(a, "Caramel")
    a = AddIn(a, "Boba")

    assert "Ice" in a.description()
    assert "Caramel" in a.description()
    assert "Boba" in a.description()
    assert "with" in a.description()
