# adrestia-getting-started

(c) 2018-2019 Sam Caldwell.  See LICENSE.txt

## Author
Sam Caldwell <mail@samcaldwell.net>

## Source Repo:
        git@github.com:sam-caldwell/adrestia-getting-started.git

## Description
This repository contains a boilerplate used for all Adrestia Python
projects.  This is intended to take setuptools and other common tooling
and establish a quick way to get started with a new project with a minimal
amount of time.

Call this the lazy programmer's approach to starting
your work.

## Getting Started
### To Start a new project...
* Create a new code repository in bitbucket or github.
* Clone this project:
    ```
        git clone https://github.com/sam-caldwell/adrestia-getting-started.git
    ```
* Execute `python3 setup.py init` and answer the questions.
* Update setup/CLASSIFIERS.txt
* Commit your initial state and push the code up to your remote repo.
* Start writing code.

### What we do for you...
* We have setup setuptools.
* We have destroyed the cloned git repo and created a new repo for your project.
* We have configured your git repo with our minimum standards.
    * Your new remote repo will be configured as origin.
    * Todo: Add a git hook to require all commits to first pass linting.
* We have used your answers to the initialization questions to
  setup your project so setup.py and other tooling uses the same information
  all the time (and you don't have to maintain it separately down the road).
* We have committed your initial state.


