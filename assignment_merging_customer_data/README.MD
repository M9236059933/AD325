# Merging Customer Data – Coding Interview Solution

## Clarifying Questions

* Can customerData2 be empty?
* What should we do if both arrays contain the same customer ID (duplicate)?

## Files

- `main.py` — main function
- `test.py` — unit tests
- `diagram.png` — flowchart

## Tests

```
python -m unittest test.py
```

## Time and Space 

***Time Complexity: O(m + n).*** We go through each element once, from the end.

***Space Complexity: O(1).*** Everything is done in-place. No extra arrays.
