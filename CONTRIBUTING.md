# Contributing to Test Calculator

Thank you for considering contributing to this project!

## Getting Started

1. Fork the repository
2. Clone your fork locally
3. Install development dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

## Development Workflow

### Running Tests

Always run tests before submitting a PR:

```bash
pytest tests/ -v
```

For coverage report:

```bash
pytest tests/ --cov=src --cov-report=term-missing
```

### Code Style

- Follow PEP 8 guidelines
- Use type hints for all function signatures
- Write docstrings for all public functions
- Keep functions small and focused

### Commit Messages

Use conventional commits format:

- `fix:` for bug fixes
- `feat:` for new features
- `docs:` for documentation changes
- `test:` for test additions/modifications
- `refactor:` for code refactoring

Example:
```
fix: handle division by zero in calculator

- Add validation for divisor being zero
- Raise ValueError with descriptive message
- Add test case for edge case
```

## Pull Request Guidelines

1. **One bug/feature per PR** - Keep PRs focused
2. **Include tests** - All bug fixes must include a test case
3. **Update docstrings** - Keep documentation current
4. **Maintain backwards compatibility** - Don't break existing API

### PR Template

Please fill out the PR template completely:
- Summary of changes
- Related issue number
- Test plan
- Breaking changes (if any)

## Bug Bounties

Some issues have bounty labels with rewards:
- `bounty` - General bounty issues
- `$50`, `$100`, etc. - Specific reward amounts

To claim a bounty:
1. Comment on the issue that you're working on it
2. Submit a PR that fixes the issue
3. Ensure all tests pass
4. Wait for review and merge

## Code of Conduct

Be respectful and constructive in all interactions.

## Questions?

Open an issue with the `question` label.
