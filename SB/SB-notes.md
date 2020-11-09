SB: turboPy Basics
==================

The need for a framework
------------------------

**NOTE: equations and figures referenced below are to those in the [preprint of the turboPy paper](https://arxiv.org/pdf/2002.08842.pdf). There is now a [final published version of the turboPy paper](https://doi.org/10.1016/j.cpc.2020.107607).**

- Example physics problem [Eqs. 1-4]
- Numerical solution [Fig. 2]
- Possible workflow [Fig. 3] and implications for class design
- Note that details for given problem are mostly at "PhysicsModule" level

The framework of turboPy
------------------------

- "Core" vs "apps"
- Core of turboPy [Fig. 1]
- Example app [ChargedParticle and EMWave PhysicsModules]

Live Example
------------

- Clone turboPy
- Set up conda env for turboPy
- Clone example problem
- Run Example
- Plot outputs

What we will be doing
---------------------

- turboPy core: mostly documentation and testing
- turboPy apps:
    - particle-in-field: documentation and testing
    - beam-driven-breakdown: 1D model of how a pulsed electron beam can form a plasma in a low-pressure gas
    - Flux-Corrected-Transport: solve fluid equations with FCT algorithm
    - Advanced particle pusher: implement new algorithm
    - Particle-pusher test app:
        - Volume preservation is discussed in some of the references.
        - Maybe we can think of some kind of app that is optimized to test the quality of volume preservation.  This hypothetical app would say “plug in your algorithm and I will tell you how well volumes in phase space are preserved.”
    - More ideas?
