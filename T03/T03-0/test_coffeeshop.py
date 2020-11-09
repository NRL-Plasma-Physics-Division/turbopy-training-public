from coffeeshop import beverage, drink_with_toppings
# not the decorater version of it that i'm testing

def test_price():
    # tests price on full order
    caroline_order = drink_with_toppings(beverage('green tea', 's'))
    assert caroline_order.cost == 2.2


def test_free_first_topping():
    # test if first topping is free
    caroline_order = drink_with_toppings(beverage('coffee', 'm'), ['soy milk'])
    assert caroline_order.cost == 2.5
    caroline_order = drink_with_toppings(beverage('coffee', 'm'), ['soy milk', 'simple syrup'])
    assert caroline_order.cost == 2.75


def test_size():
    # tests if size is correctly recorded
    caroline_order = beverage('coffee', 's')
    assert caroline_order.size == 's'


def test_toppings():
    # make sure toppings are correct price
    bev = beverage('coffee', 'm')

    two_percent = drink_with_toppings(bev, ['2% milk'])
    soy = drink_with_toppings(bev, ['soy milk'])
    almond = drink_with_toppings(bev, ['almond milk'])
    caramel = drink_with_toppings(bev, ['caramel'])
    assert two_percent.cost == 2.5
    assert soy.cost == 2.5
    assert almond.cost == 2.5
    assert caramel.cost == 2.5


    ice = drink_with_toppings(bev, ['ice'])
    simple_syrup = drink_with_toppings(bev, ['simple syrup'])
    assert ice.cost == 2.5
    assert simple_syrup.cost == 2.5

    boba = drink_with_toppings(bev, ['boba'])
    assert boba.cost == 2.5

    espresso_shot = drink_with_toppings(bev, ['espresso shot'])
    assert espresso_shot.cost == 2.5

    fun_drink = drink_with_toppings(bev, ['boba', 'ice', 'espresso shot'])
    assert fun_drink.cost == 4.25
