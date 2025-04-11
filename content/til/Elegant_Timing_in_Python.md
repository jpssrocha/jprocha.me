+++
date = '2025-02-23T14:34:16-03:00'
draft = false
title = 'Elegant Timing in Python - ft. context managers!'
+++

Frequently when testing out different algorithms and strategies we need to run
some sort of bench marking on blocks of the program. Some time ago i had to do
it for the many steps of a simulation and was reflecting on a good timing
structure. While traditional bench marking tools like cProfile are quite good
for getting an overview, when more refined timing of code blocks is necessary
usually we end up resorting to manually use something like the time library to
do something like this:

```python
from time import time

tic = time()

# Code goes here

toc = time()

print(f" Took: {toc - tic}")
```

While this gets the work done, it can become quite cumbersome when you need to
track many blocks (even wrong sometimes). These days i was doing so and
realized it could be much more elegant using some Python functionalities.

# Tip \#1 - Use `perf_counter`

On the example above i've used the `time` function on purpose because i see
many people using it when it should be using the `perf_counter` function
instead . The time function is not appropriate for profiling purposes, it's
meant for time stamping because of how it is implemented (take a look at [1]
for more details). The correct code would be:

```python
from time import perf_counter

tic = perf_counter()

# Code goes here

toc = perf_counter()

print(f" Took: {toc - tic}")
```

# Tip \#2 - Use a context manager

Now, imagine doing the tracking above with multiple test points? It would have
many blocks wrapped around `perf_counter` calls - how ugly! - but no need to
worry, Python idioms got you covered.

To time stuff elegantly we can use one of the most elegant Python idioms: a
context manager. Context managers are commonly used to manage some resource
like a file handler or a database connection, nonetheless they can be used for
any kind of context, e. g. in the context where were measuring execution
times.

Usually they can be defined in two ways: as generators or as classes with the
methods `__enter__` and `__exit__` defined on it. Let's take a look at the first
case:

```python
from contextlib import contextmanager

@contextmanager
def timer():
    try:
        tic = perf_counter()
        yield
    finally:
        print(f"took: {perf_counter() - tic}")
```

In this case we need to import the `contextmanager` decorator to convert the
function in an object that interacts with Python's data model. It can be used
this way:

```python
with timer():
    sleep(0.1) # Code would go here!
```

For quick implementation of functionality the first approach is best, but these
days i was experimenting with the second way and realized how handy it is.
Let's take a look at it in tip number 3.

# Tip \#3 - Define the context manager as class for extra functionality 

With a context manager manager defined as a class we get extra flexibility
since we can use all the tricks that object orientation can give to us! Let's
look at a basic implementation of a timer using this approach:


```python
from dataclasses import dataclass

@dataclass
class Timer:
    _elapsed_time: float = 0

    def __enter__(self):
        self._current_time = perf_counter()

    def __exit__(self, type, value, traceback):
        self._elapsed_time += perf_counter() - self._current_time

    def get_elapsed_time(self):
        return self._elapsed_time
```

In this example i've already used another Python handy builtin: **dataclasses**, the fact that 
this way of defining a context manager is a class allows me to use the dataclass decorator 
to get extra functionality to easily handle internal state. This simple tool makes possible
to elegantly time arbitrary blocks of code. For example, inside an intricate loop:

```python
t = Timer()
t2 = Timer()

for i in range(100):
    with t:
        sleep(0.1)

    with t2:
        sleep(0.05)

    with t:
        sleep(0.1)


print(t.get_elapsed_time())
print(t2.get_elapsed_time())
```

Now imagine the extra features one could implement using this approach ... maybe timer
that tracks multiple points on a dictionary, or maybe a timer that generates a pandas 
dataframe for statistical analysis, possibilities are limitless!

# In summary

1. Prefer `perf_counter` over `time` for precise timing, as it’s designed for profiling.

2. Leverage context managers to encapsulate timing logic, reducing boilerplate
   and improving readability.

3. Implement class-based context managers for advanced use cases, enabling
   cumulative timing across multiple code blocks, easier state management and
   ease of customization.

By adopting these practices, developers can achieve cleaner, reusable, and more
accurate performance measurements while maintaining streamlined code

# References

- [1] [perf_counter in Python](https://www.geeksforgeeks.org/time-perf_counter-function-in-python/)
