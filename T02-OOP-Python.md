OOP With Python
===============

Prep
----
1. Complete the RealPython [OOP with Python Learning Path](https://realpython.com/learning-paths/object-oriented-programming-oop-python/)

Seminar Goals
-------------
Review Object Oriented Programming with Python and how it is used in turboPy.

Homework
--------
* Add a note to this markdown file describing at least one OOP concept used in turboPy.
* Work through the example problem below, and add your solution as `T02/T02-lastname.py`.


Notes
-----
* The "PhysicsModule" class uses inheritance to have the same basic attributes as its parent class: "DynamicFactory"
* Classes such as Simulation, Grid, and Diagnostic can be used inside the framework where we can use their attributes and methods for common issues.
* The Simulation class uses composition: it is composed of PhysicsModules, Diagnostics, ComputeTools, a clock, and a grid, all of which can function within the framework of the simulation.

Example problem
---------------
So I thought it might be helpful to see some different examples of classes in python, and have some test problems to try and solve yourselves. In the spirit of the discussion in [issue #17](https://github.com/NRL-Plasma-Physics-Division/turboPy-training/issues/17), here is an example problem. See also [issue #23](https://github.com/NRL-Plasma-Physics-Division/turboPy-training/issues/23).

## The problem
Suppose we are starting a coffee shop, and need a system to be able to enter customer's orders, and compute the cost of their order. This could be done with a series of individual classes:
```python
class coffee:
    def cost(self):
        return 2.50
    def description(self):
        return "coffee"

class tea:
    def cost(self):
        return 2.50
    def description(self):
        return "tea"
``` 
While this looks fairly good, you can imagine that it could get messy fast. What do you do when a customer wants a decaf iced coffee with soy milk and caramel? Do you need separate classes for each possible combination of add-ins? And what if the price of milk goes up, and you need to change how much you charge? You'd have to go into every single class, and compute the new cost and update the code. It would be better if the computer could take care of this for you. Fortunately this is a solved problem, and something called the **decorator pattern** can be used to write clean code that is easy to debug and maintain.

## Your mission
Write classes (preferably using the decorator pattern) that implements the following menu:
Item | Cost
------------ | -------------
Coffee | $2.50
Espresso | $1.50
Black Tea | $2.50
Green Tea | $2.75

Add in item | Cost (added to base cost)
------------|---------------------------
2% milk | +$0.50
Soy milk | +$0.50
Almond milk | +$0.50
Ice | +$0.25
Simple syrup | +$0.25
Caramel | +$0.50
Boba | +$1.00
Espresso Shot | +$1.50

The classes should have a `cost` function that returns the price of the order. They should also have a `description` function that returns a string describing the item ordered.

## Steps for the solution
- [ ] Create folder `T02` for holding "solutions". 
- [ ] Review [this example code](https://github.com/faif/python-patterns/blob/master/patterns/structural/decorator.py).
- [ ] Create your own python code to solve the coffee-shop problem described above. Use the decorator pattern as in the example above.

Bonus items:
- [ ] First add-in is free
- [ ] Implement sizes, small/medium/large, and set prices for the different sizes.

@NRL-Plasma-Physics-Division/interns I'm looking forward to seeing your ideas for this example.
