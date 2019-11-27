# TOPyN: Typed Opinionated PYthon Normalizer
<p>
    <a href="https://github.com/lleites/topyn/actions"><img alt="Actions Status" src="https://github.com/lleites/topyn/workflows/Test/badge.svg"></a>
    <a href="https://github.com/lleites/topyn/actions"><img alt="Actions Status" src="https://github.com/lleites/topyn/workflows/Topyn/badge.svg"></a>
    <a href="https://coveralls.io/github/lleites/topyn?branch=HEAD"><img alt="Coverage Status" src="https://coveralls.io/repos/github/lleites/topyn/badge.svg?branch=HEAD"></a>
    <a href="https://github.com/lleites/topyn/blob/master/LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg"></a>
    <a href="https://pypi.org/project/topyn/"><img alt="PyPI" src="https://img.shields.io/pypi/v/topyn"></a>
</p>

## About
<p align="center">
    <img src="https://github.com/lleites/topyn/blob/master/scooter.svg" alt="Scooter" width="300"/>*
</p>
Python is quite a flexible language, something that is not so good if you start working in mid level size projects and/or in teams.
Over the time we have found a set of rules that makes working with Python in this context easier, and once you get you use to them you want to apply them to every small Python snippet that you write.

The problem is that these rules depend on a set of packages and config files, and every time we change our mind about one rule, or add new ones, we need to update multiple projects.
Topyn solves this by providing in one single place all the tools and configurations we use in our projects.

All the configurations are part of the project (`topyn/configs`) and is not the purpose of this project to make them flexible, if you need that please check the packages that we use, and run them with your configuration.

## Install
`pip install topyn`

## Command line
There are two possible arguments:
* `path` is the path that you want to check, if it is empty it defaults to the current directory.
* `--fix` if you use this flag topyn will try to fix the code for you

### Examples
Check the code inside directory_with_code : `topyn directory_with_code`

Check the code inside current directory : `topyn`

Check the code inside current directory and try to fix it: `topyn --fix`

### `topyn --help` output

```
Typed Opinionated PYthon Normalizer

positional arguments:
  path        path to topynize (default: .)

optional arguments:
  -h, --help  show this help message and exit
  --fix       try to fix my code (default: False)
  --version   show program's version number and exit
```

### `topyn` output
✅
```
➡️ Checking formatting ...
All done! ✨ 🍰 ✨
8 files would be left unchanged.
➡️ Checking rules ...
➡️ Checking types ...
✅ Everything is OK! 😎"
```
🔴 
```
➡️ Checking formatting ...
All done! ✨ 🍰 ✨
1 file would be left unchanged.
➡️ Checking rules ...
➡️ Checking types ...
tests/resources/wrong_types/wrong_types.py:2: error: Incompatible return value type (got "int", expected "str")
Found 1 error in 1 file (checked 1 source file)

🔴 Sadly, types failed 😢
```


## Tools included

### [Flake8](https://github.com/PyCQA/flake8)
flake8 is a command-line utility for enforcing style consistency across Python projects

#### Flake8 plugins
* #### [flake8-bugbear](https://github.com/PyCQA/flake8-bugbear)
  A plugin for flake8 finding likely bugs and design problems in your program. Contains warnings that don't belong in pyflakes and pycodestyle. 
* #### [flake8-print](https://github.com/JBKahn/flake8-print)
  Check for `print` statements in python files.
* #### [flake8-comprehensions](https://github.com/adamchainz/flake8-comprehensions)
  A flake8 plugin that helps you write better list/set/dict comprehensions.
* #### [pep8-naming](https://github.com/PyCQA/pep8-naming)
  Naming Convention checker for Python (PEP 8)
### [Black](https://github.com/psf/black)
The Uncompromising Code Formatter
### [Mypy](https://github.com/python/mypy)
Optional static typing for Python (PEP 484) 

## Contributors
Leandro Leites Barrios : Main developer

Denada Korita : UX & Documentation consultant 

---
\* scooter icon source: [icons8](https://icons8.com/)
