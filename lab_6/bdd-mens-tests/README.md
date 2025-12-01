# BDD Mens Page Tests

This project contains BDD tests for the Mens page of the Elite Shoppy website using Python, Behave, and Selenium.

## Structure

- `features/`: Contains the Gherkin feature files describing the test scenarios.
- `features/steps/`: Contains the Python step definitions for the scenarios.
- `pages/`: Contains the Page Object Models.
- `requirements.txt`: List of dependencies.

## Prerequisites

- Python 3.x
- Chrome Browser (or Firefox if configured)

## Installation

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running Tests

To run all tests:
```bash
behave
```

To run a specific feature:
```bash
behave features/mens_page.feature
```
