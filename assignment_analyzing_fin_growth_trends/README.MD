# TextWise Solutions – Analyzing Financial Growth Trends

## Clarifying Questions

* Are all elements guaranteed to be integers?
* Do we need to preserve duplicate values?

## Files

- `main.py` — main function
- `test.py` — unit tests
- `diagram.png` — flowchart

## Tests

```
python -m unittest test.py
```

## Time and Space 

***Time Complexity: O(n * log n).*** We iterate through the input array once O(n). Python built-in sort has time complexity of O(n log n). So, the final time complexity is O(n log n).
***Space Complexity: O(n).*** O(n), because we store the result in a new list the same size.
