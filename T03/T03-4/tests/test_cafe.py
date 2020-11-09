import sys
import pytest

sys.path.append('./')
from cafe import Base, AddOns


@pytest.fixture(name='coffee')
def fixture_coffee():
    """Creates fixture for a coffee Base object"""
    return Base('coffee', 'grande')


def test_cost(coffee):
    """Checks the price attribute and cost() function of the Base object"""
    assert coffee.price == 3.5
    assert coffee.cost() == f'${coffee.price:.2f}'


def test_addon(coffee):
    """Checks that the AddOns decorator class works and for the description() function"""
    drink = AddOns(coffee, 'ice', False)
    assert 'with ice' in drink.description()
