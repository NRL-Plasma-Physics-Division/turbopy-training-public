Git and Github (and Markdown)
=============================

Prep
----
1. Read **Chapter 1. Getting Started** in the [Pro Git book](https://git-scm.com/book/en/v2).
2. Install `git` following the directions in [section 1.5 of the Pro Git book](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).
3. Complete the RealPython courses: [Python Git and Github Intro](https://realpython.com/courses/python-git-github-intro/)
4. Review [15 rules for communicating at GitHub](https://ben.balter.com/2014/11/06/rules-of-communicating-at-github/)
5. Complete [this markdown lesson](https://www.markdowntutorial.com) and read [Mastering Markdown (for Git)](https://guides.github.com/features/mastering-markdown/).

Seminar Goals
-------------
Discuss what we learned about Git and Github and how it applies to the project.
 
Homework
--------
1. Fork and clone the `turboPy-training` repo
2. Create a `dev` branch and commit/push some notes to the Notes section of this markdown file
3. Create a pull request to merge your changes to `turboPy-training` main
4. Coordinate with the other interns to divide and conquer to finish step 2 of the Seminar Workflow in the README file for all scheduled seminars.

Notes
-----
- Be sure to name branches and files logically and succinctly so as to minimize confusion between editors.
- When forking the organization repository it is possible that not all branches will show up on your personal repository page.
  Double check that all branches appear on your local Git client and if they do then there shouldn't be an issue.
- Always put a commit summary in the imperative form.
- Make sure your local repo is up to date with the upstream to avoid merge conflicts. 
- Generally, it's not a good idea to commit directly to main. Instead, create a development branch and merge it with a pull request on github.
- You can force a line break in markdown by putting two spaces, or a backslash, at the end of a line. Learned about it [here](https://gist.github.com/shaunlebron/746476e6e7a4d698b373).
- You can also make text _italicized_ or **bold** by surrounding the text with underscores or asterisks like so: \*italics* or \_italics_ and \*\*bold** or \_\_bold__.
- [Updating Fork](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/syncing-a-fork) (From upstream main branch):
```shell
# start in local main
git checkout main
# add remote for upstream
git remote add upstream https://github.com/NRL-Plasma-Physics-Division/turboPy-training.git
git fetch upstream
# merge the copied PPD main files in upstream to main
git merge upstream/main 
# push the changes to origin (your fork, implied)
git push 
```
- You can fetch someone else's fork/branch (see [the inspirational gist](https://gist.github.com/elfrank/c08256de9c15e41e1781)):
```shell
# add remote for batman's iambatman repo
git remote add batman git@github.com:batman/iambatman.git
# fetch batman's code in iambatman
git fetch batman 
# switch to savegotham branch, naming it local-branch-name locally
git checkout -b local-branch-name batman/savegotham 
```
