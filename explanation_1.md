# Explanation Problem 1

## Least Recently Used Cache 

Data Structures

Collections Used:
    1. Python Collections.Deque (https://docs.python.org/3/library/collections.html#collections.deque)
    2. Dict() collection.

Both Deque and Dictionary maintain O(1) time complexity.
    1. Dequeue methods .popLeft() and .append()
    2. Dict methods .get() and .update()

I took advantage of key value pairs from Dict() to quickly return cache entries.
Dequeue implementation referring to the oldest entry in the cache that is replaced by a new one.


Deque has a space complexity of O(N). You only add memory that holds current values and possible successors. 


