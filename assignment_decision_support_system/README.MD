# Decision Support System for a Financial Institution Using Binary Tree – Coding Interview Solution

## Clarifying Questions

* Can the tree be unbalanced?
* Can there be repeated questions or answers?

## Files

- `main.py` — main function
- `test.py` — unit tests
- `diagram.png` — flowchart

## Tests

```
python -m unittest test.py
```

## Time and Space 

***Time Complexity: O(n).*** O(n) because we visit each node exactly once during the traversal.
***Space Complexity: O(h - tree height).***  O(h), where h is the height of the tree, due to the recursive call stack — this can range from O(log n) in a balanced tree to O(n) in the worst case (skewed tree).