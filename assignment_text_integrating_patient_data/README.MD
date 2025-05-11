# TextWise Solutions – Integrating Patient Records from Two Healthcare Providers

## Clarifying Questions

* Are duplicate SSNs allowed in the merged result?
* Can SSN values be equal, and are they unique within a single list?

## Files

- `main.py` — main function
- `test.py` — unit tests
- `diagram.png` — flowchart

## Tests

```
python -m unittest test.py
```

## Time and Space 

***Time Complexity O(n + m)*** 
We traverse each node in both input lists exactly once.
At every step, we compare the current nodes of both lists and attach the smaller one to the merged result.
Finally we append remaining nodes.

***Space Complexity O(1)*** 
We do not create new nodes, just reuse the existing nodes from the input lists.