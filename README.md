# Test Calculator

A simple Python calculator package used for testing the AUTONOMIX bounty hunting agent.

## Installation

```bash
pip install -e ".[dev]"
```

## Usage

```python
from src.calculator import add, subtract, multiply, divide

result = add(2, 3)  # 5
result = divide(10, 2)  # 5.0
```

## Running Tests

```bash
pytest tests/
```

## Known Issues

This codebase has several intentional bugs for testing purposes:
- Division by zero not handled
- Off-by-one errors in utility functions
- Input validation gaps

See the GitHub Issues for bounties on fixing these bugs.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting PRs.

## License

MIT
