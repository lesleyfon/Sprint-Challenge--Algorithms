# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```python
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```

```
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```

```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

### Solution

Since the Number of floors is like a sorted list i will use a binary search to determine the f floor.

1. First Create a variable to represent the middle floor.
2. Check if the egg can get broken from the middle floor and if dropping an egg from the floor below it will not break. if so we have found f
3. Check is the egg is broken or not.
4. If the egg gets broken being dropped from the middle floor, we want to discard the top floors and set the new top floor to be the middle.
5. If the egg doesn't get broken from being dropped at the the middle floor, we want to set the new starting floor to the middle. and keep keep repeating this step until we have found a floor where middle floor minus one doesn't break an egg and middle floor breaks an egg
