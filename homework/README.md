# Homework Directory

## CS 107 Homework Workflow

The "Homework Setup" text below has been copied from the 2020-CS107 [Course Workflow site](https://harvard-iacs.github.io/2020-CS107/pages/coursework.html).

#### Homework Setup

* Make sure your master branch is up-to-date.
    * Use the git pull to update your local master branch so it is in-sync with your remote master branch.
* From your local master Git branch, create a new development branch called HW3-dev.
    * Use the git checkout command to create a new local development branch.
    * The teaching staff will only be grading the work you do on this development branch. You will lose 5 points if you do not do your development on the HW3-dev branch. You are free to make other branches off of HW3-dev, say for individual problems, but you are responsible for making sure you merge these additional branches into the HW3-dev branch.
* Within your homework/ directory, create subdirectory HW3/.
* Under the HW3/ directory, create subdirectory HW3-final/.
* Only files within HW3-final/ will be graded. HW3-final/ should consist of one python file for each problem:
    * P1.py, P2.py, P3.py, P4.py
    * Each file should run and return the required output.

#### Branch Organization

|Master Branch|HW#-dev Branch|
|:---|:---|
| Initial README, from setup | Current hw, in progress |
| Merged dev branch, after grading | Completed hw, to be submitted |
