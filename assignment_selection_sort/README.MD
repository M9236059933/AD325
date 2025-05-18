# Implementing and Analyzing Selection Sort


## Files

- `main.py` — main function
- `test.py` — unit tests

## Tests

```
python -m unittest test.py
```

## Time and Space 

***Time Complexity: O(n²)*** We loop through the array with nested loop. For each element, we search the rest of the array to find the minimum. This results in about n × (n - 1) / 2 comparisons, which gives us O(n²).

***Space Complexity: O(n)*** Selection Sort is an in-place algorithm. It doesn’t use any extra memory beyond a few variables (like index tracker and swap variable), so the space usage stays constant O(1).

***Stability:*** Selection sort is NOT stable by default. It may swap equal elements and change their relative order. Example: [4a, 4b, 3] => [3, 4b, 4a] after sorting

Another example:
```
students = [
    {"name": "Alice", "score": 90},
    {"name": "Bob", "score": 80},
    {"name": "Charlie", "score": 90},
]
```

Charlie may be in front of Alice, although they have the same points.