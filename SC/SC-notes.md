SC: turboPy Core Project
========================

What is Continuous Integration?
-------------------------------

There are ***a lot*** of phrases floating around in the software development universe: continuous integration, continuous development/deployment/delivery, DevOps, SecDevOps, DevSecOps...

We are just going to use the phrase Continuous Integration (CI), and here is what we mean:

- Merging small code changes often
- Testing and documenting as we go
- Integrating with (lightweight, but robust) project governance
  - Aspiring to test-driven development (writing tests after a [code spike](https://en.wikipedia.org/wiki/Spike_(software_development)) is O.K.)
  - Managing Project Boards (cards)
  - Managing milestones/releases
- Utilizing [TravisCI](https://travis-ci.org), [GitHub Actions](https://github.com/features/actions), [CircleCI](https://circleci.com), [gitlab-runner](https://docs.gitlab.com/runner/), [ReadTheDocs](https://readthedocs.org), etc to automate tests, build documentation, deploy products, build release downloads, run linters, create badges...pretty much anything we would want to automate and/or report

Why do CI? 
----------

Because it:
- Frees up our minds to develop
- Keeps us all honest
- Distributes the workload
- Keeps us all on the same page
- Reduces accumulation of [technical debt](https://en.wikipedia.org/wiki/Technical_debt)

An example of CI in action: [nepc](https://github.com/USNavalResearchLaboratory/nepc)
-------------------------------------------------------
What we will do:
- fork and clone nepc
- quick tour of nepc including `nepc` folder and `CS` class
- `tests` folder and `conftest.py` file
- `.travis.yml` and [nepc build on TravisCI](https://travis-ci.org/github/USNavalResearchLaboratory/nepc)
- demo adding `assert` to `test_CS_class()` in `tests/test_nepc.py`
- [WIP] pull request, trigger TravisCI build
- `docs` folder and docstrings in source code
- `.readthedocs.yml` and [nepc documentation on ReadTheDocs](https://nepc.readthedocs.io/en/latest/)

What we didn't get to:
- [nepc project on ReadTheDocs](https://readthedocs.org/projects/nepc/)

Getting started with the turboPy core project
---------------------------------------------
- Check out the [turboPy issues](https://github.com/NRL-Plasma-Physics-Division/turbopy/issues)
- Start writing tests and documentation for turboPy as you work through the RealPython Learning Paths