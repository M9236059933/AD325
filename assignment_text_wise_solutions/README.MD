# TextWise Solutions – Coding Interview Solution

## Clarifying Questions

* Should we handle None or invalid input types?

## Files

- `main.py` — main function
- `test.py` — unit tests
- `diagram.png` — flowchart

## Tests

```
python -m unittest test.py
```

## Time and Space 

***Time Complexity: O(n).*** We process one character per recursive call, so for a string of length n, there are n calls.
***Space Complexity: O(n).*** Each recursive call adds a new frame to the call stack, so the maximum depth is n.
