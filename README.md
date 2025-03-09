# My Python Project

[![CI](https://github.com/dan-driver/my_python_project/actions/workflows/ci.yml/badge.svg)](https://github.com/dan-driver/my_python_project/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/dan-driver/my_python_project/graph/badge.svg?token=ABECRCOUG2)](https://codecov.io/gh/dan-driver/my_python_project)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![flake8](https://img.shields.io/badge/lint-flake8-green)](https://flake8.pycqa.org/)
[![mypy](https://img.shields.io/badge/type%20checker-mypy-blue)](http://mypy-lang.org/)
[![pylint](https://img.shields.io/badge/lint-pylint-yellowgreen)](https://pylint.pycqa.org/)

This is a base python project with project configuration with QA and CI setup as a starting point for other projects.

## Overview
This project is a Python application that includes a main module and corresponding tests. It is set up with various tools for code quality and continuous integration.

## Features
- Main application logic implemented in `my_python_project/main.py`
- Unit tests using `pytest` located in `tests/test_main.py`
- Code linting with `Pylint` and `Flake8`
- Type checking with `MyPy`
- Automated testing and linting via GitHub Actions

## Getting Started

### Prerequisites
Make sure you have Python 3.6 or higher installed on your machine.

### Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/my-python-project.git
   ```
2. Navigate into the project directory:
   ```
   cd my-python-project
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

### Usage
To run the main application, execute:
```
python my_python_project/main.py
```

### Running Tests
To run the tests, use:
```
pytest tests/
```

### Linting
To check the code quality, run:
```
pylint my_python_project/
```
or
```
flake8 my_python_project/
```

### Type Checking
To perform type checking, execute:
```
mypy my_python_project/
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.