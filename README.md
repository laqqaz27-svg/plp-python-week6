# Week 6 - Safe Functions

## Assignment: Safe Functions

This assignment practices using `try` and `except` to handle errors and keep Python programs from crashing.

### Files

- `safe_tools.py` - Contains three safe functions for division, number conversion, and dictionary field lookup.
- `unbreakable.py` - Demonstrates how `try` and `except` can safely handle invalid number input.
- `README.md` - Describes the assignment and explains error handling.

### Why can the `if` check not catch `abc` on its own?

An `if` check cannot catch `abc` when using `int()` because the conversion happens before the program can continue to the check. The `int("abc")` operation raises a `ValueError`, so we use `try` and `except` to handle the error safely.