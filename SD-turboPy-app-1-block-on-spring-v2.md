TurboPy App Project 1: Block-on-Spring V2
=========================================

Prep
----
This app will be a slight variation to the existing [block-on-spring](https://github.com/NRL-Plasma-Physics-Division/block-on-spring) example app (referred to as "Version 1").

Version 1 of the app solves for the motion of a block on a spring.

In version 1 of the app, the equations of motion are solved using the [forward Euler method](https://en.wikipedia.org/wiki/Euler_method). While this works, the method has low accuracy, and is known to introduce systematic errors in the energy of the block.

For version 2 of the app, we will implement a better "particle pusher" for solving the equations of motion for the block. We will use [the leapfrog method](https://en.wikipedia.org/wiki/Leapfrog_integration).

Seminar Goals
-------------
Learn about development of turboPy apps by making a slight modification to the existing block-on-spring app.

Learn more about numerical integration methods.

Learn more about how to use the `ComputeTool` class in turboPy.

Notes
-----

For more information about integration methods see:
- [Symplectic integration](https://en.wikipedia.org/wiki/Symplectic_integrator)
- [Verlet integration](https://en.wikipedia.org/wiki/Verlet_integration)
