# TOPyN: Typed Opinionated PYthon Normalizer

## About

<img src="scooter.svg" alt="Scooter" width="600"/>

Python is a quite flexible language, something that is not soo good if you start working on mid level size projects or in teams.
Over the time we have found a set of rules that make working with Python in this context easier, and once you get you use to them you want to apply it to every small Python snippet that you do.

The problem is that this rules depend on a set of packages and config files and packages installed, and every time we change our mind about one rule we need to update multiple projects.
Topyn solve this by providing in one single place all the tools and configurations we use in our projects.

All the configurations are part of the project and is not the porpoise of this project to make them flexible, if you need that please check the packages that we use, a d run them with your configuration.

## Command line
```
Typed Opinionated PYthon Normalizer

positional arguments:
  path        path to topynize (default: .)

optional arguments:
  -h, --help  show this help message and exit
  --fix       try to fix my code (default: False)
  --version   show program's version number and exit
```


## Tools included

### [Flake8](https://github.com/PyCQA/flake8)
flake8 is a command-line utility for enforcing style consistency across Python projects

#### Flake8 plugins
#### [flake8-bugbear](https://github.com/PyCQA/flake8-bugbear)
A plugin for Flake8 finding likely bugs and design problems in your program. Contains warnings that don't belong in pyflakes and pycodestyle. 
#### [flake8-print](https://github.com/JBKahn/flake8-print)
Check for Print statements in python files.
#### [flake8-comprehensions](https://github.com/adamchainz/flake8-comprehensions)
A flake8 plugin that helps you write better list/set/dict comprehensions.
### [Black](https://github.com/psf/black)
The Uncompromising Code Formatter
### [Mypy](https://github.com/python/mypy)
Optional static typing for Python (PEP 484) 
