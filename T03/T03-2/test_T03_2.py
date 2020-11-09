'''Runs tests on T02_2.py'''
import pytest
from T03_2 import Drink, BASES, SIZES, ADD_INS

@pytest.fixture(name='drink')
def fixture_drink():
    '''Fixture for drink class'''
    return Drink('Coffee', 'Small', 2.00)

def test_init(drink):
    '''Tests the Drink class initializer'''
    assert drink.base == 'Coffee'
    assert drink.size == 'Small'
    assert drink.price == 2.00
    assert drink.add_ins == []

def test_cost(drink):
    '''Tests the Drink class' cost method'''
    assert drink.cost() == '$2.00'
    drink.add('Ice')
    assert drink.cost() == '$2.00'
    drink.add('Boba')
    assert drink.cost() == '$3.00'

def test_add(drink):
    '''Tests the Drink class' add method'''
    drink.add('Ice')
    assert drink.add_ins == ['Ice']
    assert drink.price == 2.25

def test_description(drink):
    '''Tests the Drink class' description method'''
    assert drink.description() == 'Small Coffee'
    drink.add('Ice')
    assert drink.description() == 'Small Coffee with Ice'

def test_dics():
    '''Tests the dictionaries in the main program'''
    assert isinstance(BASES, dict)
    assert isinstance(SIZES, dict)
    assert isinstance(ADD_INS, dict)
    for i in range(len(BASES)):
        assert isinstance(list(BASES)[i], str)
        assert isinstance(BASES[list(BASES)[i]], float)
    for i in range(len(SIZES)):
        assert isinstance(list(SIZES)[i], str)
        assert isinstance(SIZES[list(SIZES)[i]], float)
    for i in range(len(ADD_INS)):
        assert isinstance(list(ADD_INS)[i], str)
        assert isinstance(ADD_INS[list(ADD_INS)[i]], float)
