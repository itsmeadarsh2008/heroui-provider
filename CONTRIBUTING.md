# Contributing to HeroUI Provider

Thank you for your interest in contributing to HeroUI Provider! This document provides guidelines and instructions to help you contribute effectively.

## Table of Contents
- [Development Setup](#development-setup)
- [Project Structure](#project-structure)
- [Adding a New Component](#adding-a-new-component)
- [Testing Your Changes](#testing-your-changes)
- [Running Utilities](#running-utilities)
- [Coding Style](#coding-style)
- [Commit Guidelines](#commit-guidelines)
- [Pull Request Process](#pull-request-process)

## Development Setup

1. Fork the repository
2. Clone your fork:

   ```bash
   git clone https://github.com/your-username/heroui-provider.git
   cd heroui-provider
   ```

3. Install development dependencies:

   ```bash
   pip install -e '.[dev]'
   ```

4. Set up the examples environment:

   ```bash
   cd examples
   pip install -r requirements.txt
   pip install -e ..
   ```

## Project Structure

```
heroui-provider/
├── src/                    # Source implementation directory
│   ├── provider/           # Base provider component
│   ├── button/             # Button component
│   ├── card/               # Card component
│   └── ...                 # Other components
├── heroui/                 # Public API package
│   ├── __init__.py         # Exports all components
│   └── examples.py         # Example usage
├── examples/               # Example applications
│   ├── examples/           # Example components
│   ├── assets/             # Static assets
│   └── requirements.txt    # Example dependencies
├── utils/                  # Utility scripts
├── pyproject.toml          # Project configuration
└── README.md               # Project documentation
```

## Adding a New Component

1. Create a new directory in `src/` for your component:

   ```bash
   mkdir -p src/your_component
   ```

2. Add the necessary files:

   ```bash
   touch src/your_component/__init__.py
   touch src/your_component/your_component.py
   touch src/your_component/py.typed  # For type hints
   ```

3. Implement your component in `your_component.py`:

   ```python
   import reflex as rx
   from typing import Any, Literal, Optional

   lib_deps: list = ["@heroui/theme", "@heroui/system", "framer-motion"]

   class YourComponent(rx.Component):
       """Your component description.

       Attributes:
           library: The library the component belongs to.
           lib_dependencies: Dependencies required by the component.
           tag: The tag name for the component.
           # Add your component attributes here
       """

       library = "@heroui/your-component"
       lib_dependencies: list = lib_deps
       tag = "YourComponent"

       # Add your component props here
       variant: rx.Var[Literal["option1", "option2"]] = "option1"
       # ...

       # Add your component events here
       on_click: rx.EventHandler[lambda x: x]
       # ...
   ```

4. Update the `__init__.py` file:

   ```python
   from .your_component import YourComponent

   your_component = YourComponent.create
   ```

5. Update the main `heroui/__init__.py` file to import your component:

   ```python
   # In heroui/__init__.py
   from src.your_component import *
   ```

6. Run the update_pyproject utility to register your component:

   ```bash
   python utils/update_pyproject.py
   ```

## Testing Your Changes

1. Navigate to the examples directory:

   ```bash
   cd examples
   ```

2. Import and use your component in `examples/examples.py`:

   ```python
   from heroui import your_component
   
   # Add your component to the example app
   ```

3. Run the example application:

   ```bash
   reflex run
   ```

4. Visit `http://localhost:3000` in your browser to test your component.

## Running Utilities

The project includes utility scripts to help with development:

- Update project configuration:

  ```bash
  python utils/update_pyproject.py
  ```

Run this utility periodically, especially after adding new components, to keep the project configuration up-to-date.

## Coding Style

Please follow these style guidelines:

- Use [PEP 8](https://www.python.org/dev/peps/pep-0008/) for Python code
- Add docstrings to all classes and methods
- Include type hints for all function parameters and return values
- Format your code with black before submitting

## Commit Guidelines

- Use clear, descriptive commit messages
- Start with a verb in the present tense (e.g., "Add", "Fix", "Update")
- Reference issue numbers when applicable
- Keep commits focused on a single change

Example:

```
Add Avatar component with size variants

- Implement basic Avatar component
- Add size variants (sm, md, lg)
- Include image and initial fallback support
- Update examples to showcase the component
```

## Pull Request Process

1. Ensure all code working properly and your code follows the style guidelines
2. Update documentation to reflect your changes
3. Submit a pull request with a clear description of the changes
4. Address any feedback from code reviews

Thank you for contributing to HeroUI Provider!
