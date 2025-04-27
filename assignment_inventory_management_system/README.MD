# Inventory Management System Update – Coding Interview Solution

## Clarifying Questions

* What if duplication would go beyond the array?
* What should we do if we have 2 zeros in a row?

## Files

- `main.py` — main function
- `test.py` — unit tests
- `diagram.png` — flowchart

## Tests

```
python -m unittest test.py
```

## Time and Space 

***Time Complexity: O(n).*** We go through array once to count zeros O(n), and once again from the end with the while loop O(n). In total, the time complexity is O(n).
***Space Complexity: O(1).*** Everything is done in-place, we create only couple variables. No extra arrays.
