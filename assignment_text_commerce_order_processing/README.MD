# TextWise Solutions – E-Commerce Order Processing System

## Clarifying Questions

* Should duplicates be allowed?
* Is thread safety a concern?

## Files

- `main.py` — main function
- `test.py` — unit tests
- `diagram.png` — flowchart

## Tests

```
python -m unittest test.py
```

## Time and Space 

***Time Complexity*** 

**Append Operation: O(n)**
We need to go from the head to the very last node, N steps.

**Display Operation: O(n)**
We must go through all the nodes of the list, N steps.

**Reverse Operation: O(n)**
We must go through all the nodes of the list, N steps. Reverse operation is pretty simple O(1). + Separated operation Display


***Space Complexity*** 

**Append Operation: O(1)**
We create only 1 node O(1).

**Display Operation: O(1)**
We don't create new. Only 1 temp variable.

**Reverse Operation: O(1)**
We don't create new nodes or structures, we use only 3 temp variables.


