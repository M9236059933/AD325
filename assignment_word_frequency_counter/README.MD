# TextWise Solutions – Building a Simple Word Frequency Counter | HashMap in Java

## Clarifying Questions

* Should we ignore punctuation like commas, periods, and exclamation marks?
* Can we assume input will only contain English characters?
* Do we need to handle special characters, like emojis or Unicode characters?
* Is there a maximum expected input size we should optimize for?

## Files

- `main.py` — main function
- `test.py` — unit tests
- `diagram.png` — flowchart

## Tests

```
python -m unittest test.py
```

## Time and Space 

***Time Complexity: O(n + k log k).*** 
We process each character once (lowercasing, cleaning, splitting) - O(n) and each word once (counting) - O(n). 
Sorted(frequencies): O(k log k), where k is the number of unique words
Print iterations - O(k).

***Space Complexity: O(n).***
Strings in Python are immutable, so each transformation (lower(), re.sub()) creates a new string in memory — O(n) for each.
The split() operation creates a list of words — O(n).
The frequency dictionary stores unique words — O(k).