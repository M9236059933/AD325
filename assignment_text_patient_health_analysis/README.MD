# TextWise Solutions – Patient Health Record Symmetry Analysis

## Clarifying Questions

* Should the function modify the original linked list?
* What is the expected behavior for empty or single-node lists?

## Files

- `main.py` — main function
- `test.py` — unit tests
- `diagram.png` — flowchart

## Tests

```
python -m unittest test.py
```

## Time and Space 

***Time Complexity O(n)*** 
The function performs a single pass through the linked list using two pointers (slow and fast) to find the middle — this takes O(n) time.
In the second phase, it compares the second half of the list to values stored in a stack — another O(n/2) steps.

***Space Complexity O(n)*** 
During the first half of the traversal, we store only half of the list’s values in a stack O(n/2). Without constants it's O(n).

