"""Tests the classes of the coffee shop problem"""
import pytest
from drink import Order, Size, Extra


@pytest.fixture(name="sample")
def fixture_sample():
    """Creates sample object to be used in tests

    Returns
    -------
    Order
        Order initialized to be Coffee
    """
    return Order("Coffee")


def test_order(sample):
    """Tests the constuctor, description and cost of base order class

    Parameters
    ----------
    Sample : Order
        A test drink used to test the instance, desciption and cost methods

    """
    assert isinstance(sample, Order)
    assert "Coffee" in sample.description()
    assert sample.cost() == 2.50


def test_size(sample):
    """Tests the instance, description, and cost of and order with size

    Parameters
    ----------
    Sample : Order
        A test drink used to test the instance, desciption and cost methods

    """
    size_sample = Size(sample, "Large")
    assert isinstance(size_sample, Size)
    assert "Large" in size_sample.description()
    assert size_sample.cost() == 4.50


def test_extra(sample):
    """Tests the instance, cost, description and dictionary of extras

    Parameters
    ----------
    Sample : Order
        A test drink used to test the instance, desciption and cost methods

    """
    extra_sample = Size(sample, "Large")
    extra_sample = Extra(extra_sample, ["Ice", "Boba", "Boba"])
    assert isinstance(extra_sample, Extra)
    assert "Boba" in extra_sample.description()
    real_extras = {"2% Milk": 0.50, "Soy Milk": 0.50,
                   "Almond Milk": 0.50, "Ice": 0.25,
                   "Simple Syrup": 0.25, "Caramel": 0.50,
                   "Boba": 1.00, "Espresso Shot": 1.50}
    for key in real_extras:
        assert key in Order.extras
        assert real_extras[key] == Order.extras[key]
    assert extra_sample.cost() == 6.5
    empty_extra_sample = Extra(Size(sample, "Large"), [])
    assert "None" in empty_extra_sample.description()
