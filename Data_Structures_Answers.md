Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?

O(1) since it's constant.

2. What is the space complexity of your ring buffer's `append` function?

O(1) since it's constant.

3. What is the runtime complexity of your ring buffer's `get` method?

O(n) because it's iterating once.

4. What is the space complexity of your ring buffer's `get` method?

O(n) because the algorithm has to allocate memory for the same number of items as in the input list.

5. What is the runtime complexity of the provided code in `names.py`?

O(n^2) because there are two loops to iterate over.

6. What is the space complexity of the provided code in `names.py`?

I think O(n) because the algorithm has to allocate memory for the same number of items as in the input list.

7. What is the runtime complexity of your optimized code in `names.py`?

I think it would be O(2n) because it's checking through 2 dictionaries, and iterating through a dictionary is O(n).

8. What is the space complexity of your optimized code in `names.py`?

I think it would be O(n) as well.