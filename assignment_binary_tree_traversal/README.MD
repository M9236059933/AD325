# Assignment – Comprehensive Binary Tree Traversal and Construction

## Files

- `main.py` — main functions
- `test.py` — unit tests

## Tests

```
python -m unittest test.py
```

## Short Report

***Approach:***
* Used recursion for preorder, inorder and postorder traversals.
* Used an iterative queue (BFS) for level order traversal.
* For construction, recursively found root from preorder and divided inorder list accordingly.

***Challenges:***
* Managing list slicing correctly for building the tree.
* Ensuring edge cases like empty trees were handled.

***Solution:***
* Used clear base cases in recursive functions.
* Tested with skewed and empty trees to confirm robustness.