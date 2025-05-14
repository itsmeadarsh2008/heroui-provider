# HeroUI Provider Examples

This directory contains example applications showcasing HeroUI Provider components for the Reflex web framework.

## Getting Started

### Prerequisites

- Python 3.13 or higher
- [Reflex](https://reflex.dev/) 0.7.9 or higher

### Installation

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Install the local HeroUI Provider package:
   ```bash
   pip install -e ..
   ```

3. Run the example application:
   ```bash
   reflex run
   ```

4. Open your browser and navigate to http://localhost:3000

## Example Structure

- `examples/examples.py`: Main example application showcasing various components
- `rxconfig.py`: Reflex configuration file
- `assets/`: Static assets for the example app

## Available Examples

The example application demonstrates the following components:

- Provider configuration with dark mode toggle
- Avatar component with different sizes
- Button component with various styles and states
- Card component with header, body, and footer
- Textarea component with event handling
- And more!

## Testing New Components

When developing new components, you can use this example directory to test your changes:

1. Import your new component in `examples/examples.py`
2. Add your component to the example UI
3. Run the application to test interactions and styling

## Modifying Examples

Feel free to modify these examples to test different component configurations or create new examples to showcase specific features.