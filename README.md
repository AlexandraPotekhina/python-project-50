# Gendiff
[![Actions Status](https://github.com/AlexandraPotekhina/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/AlexandraPotekhina/python-project-50/actions)
[![Github Actions Status](https://github.com/AlexandraPotekhina/python-project-50/workflows/Python%20CI/badge.svg)](https://github.com/AlexandraPotekhina/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/ba3b488889266f66e581/maintainability)](https://codeclimate.com/github/AlexandraPotekhina/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/ba3b488889266f66e581/test_coverage)](https://codeclimate.com/github/AlexandraPotekhina/python-project-50/test_coverage)

CLI utility that generates and shows a difference between two configuration files.   
Supported formats: JSON and YAML formats.   
Shows difference as a structured text ('stylish', default), plain text ('plain') or JSON.

## Usage

### CLI

```
gendiff filepath1 filepath2 [--option]
```

-h, --help: shows help message.   
-f, --format: shows difference in one of three formats: 'stylish' (default), 'plain' or 'json'.

### Gendiff library

```python
from gendiff import generate_diff

diff = generate_diff(filepath1, filepath2)
```

## Installation

```bash
python3 -m pip install --user git+https://github.com/AlexandraPotekhina/python-project-50.git
```