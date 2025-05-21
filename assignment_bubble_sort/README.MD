# Implementing and Analyzing Bubble Sort


## Files

- `main.py` — main function
- `test.py` — unit tests

## Tests

```
python -m unittest test.py
```

## Time and Space 

***Time Complexity: O(n) -> O(n²)***
Bubble Sort uses nested loops to compare and swap adjacent elements. In the worst and average cases, the algorithm still performs about n * (n - 1) / 2 comparisons, resulting in O(n²) time complexity.

However, in the optimized version, we add a flag (swapped) to check whether any swaps were made during a full pass through the array. If no swaps occurred, the array is already sorted, and we can stop early. O(n)

***Space Complexity: O(1)***
Bubble Sort is an in-place sorting algorithm, meaning it does not require additional memory
beyond maybe a few variables used for swapping. Therefore, the space complexity is constant: O(1).

***Stability:***
Bubble Sort is a stable sorting algorithm because it only swaps adjacent elements.
If two elements are equal, their relative order is preserved.

Example:

students = [
    {"name": "Alice", "score": 90},
    {"name": "Bob", "score": 80},
    {"name": "Charlie", "score": 90},
]

After sorting by score:
[
    {"name": "Bob", "score": 80},
    {"name": "Alice", "score": 90},
    {"name": "Charlie", "score": 90},
]

Alice still appears before Charlie, showing the algorithm maintains stability.