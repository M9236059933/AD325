# Implementing and Analyzing Insertion Sort


## Files

- `main.py` — main function
- `test.py` — unit tests

## Tests

```
python -m unittest test.py
```

## Time and Space 

***Time Complexity: O(n) -> O(n²)*** When the array is already sorted. The inner loop never shifts any elements O(n). When the array is sorted in reverse order. Each new element is compared and shifted all the way to the beginning n * (n - 1) / 2. O(n²)

***Space Complexity: O(1)*** Selection Sort is an in-place algorithm. It doesn’t use any extra memory beyond a few variables (like key and pointer), so the space usage stays constant O(1).

***Stability:*** Insertion Sort is stable. It only moves elements greater than the key to the right and inserts the key after all equal elements.

Example:

before
```
students = [
    {"name": "Alice", "score": 90},
    {"name": "Bob", "score": 80},
    {"name": "Charlie", "score": 90},
]
```

after
```
[
    {"name": "Bob", "score": 80},
    {"name": "Alice", "score": 90},
    {"name": "Charlie", "score": 90},
]
```

Alice stays before Charlie, preserving their original relative order — that’s stability.