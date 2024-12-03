print("\nGenerators are functions that return an object that can be iterated over. They generate inside the object lazily "
      "\nmeaning they only generate one at a time and only when asked for, so they are much more memory efficient.")

print("\nGenerators use the yield keyword rather than the return keyword. It is possible to have multiple yields in one "
      "object.")
def my_generator():
    yield 1
    yield 2
    yield 3

g = my_generator()

for i in g:
    print(i)

print("\nThe object can be iterated through slowly using the next() function. Also, once a generator object has been "
      "iterated through, it must be reinitialized again.")

def my_generator():
    yield 1
    yield 2
    yield 3

g = my_generator()

value = next(g)
print(value)

value = next(g)
print(value)

value = next(g)
print(value)

print("\nOnce the list has been iterated through and there is an attempt to iterate further, it generates a StopIteration error.")

print("\nDue to the nature of being an iterable, it is possible to use functions like sum() with the object.")
def my_generator():
    yield 1
    yield 2
    yield 3

g = my_generator()

print(sum(g))

print("\nIt is also possible to sort the object.")
def my_generator():
    yield 3
    yield 2
    yield 1

g = my_generator()

print(sorted(g))

print("\nIt is possible to use generators to create something like a countdown.")
def countdown(num):
    print("Starting")
    while num > 0:
        yield num
        num -= 1

cd = countdown(4)
value = next(cd)
print(value)
print(next(cd))
print(next(cd))
print(next(cd))

print("\nThe main advantage of using a generator is that the memory size used is a lot less compared to something "
      "like a list.")
import sys

def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums

def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1

print(firstn(10))
print(list(firstn_generator(10)))

print("\nSize difference between a data set of 1,000,000 elements.")
print("Size of regular list: ", sys.getsizeof(firstn(1000000)))
print("Size of a generator: ", sys.getsizeof(firstn_generator(1000000)))

print("\nAnother example of using a generator is generating the Fibonacci sequence.")
def fibonacci(limit):
    # 0 1 1 2 3 5 8 13 ...
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

fib = fibonacci(45)
for i in fib:
    print(i)

print("\nIt is also possible to write generator expressions which could help at times writing them more quickly.\n"
      "It has similar syntax to list comprehension but uses parentheses instead of brackets.")
mygenerator = (i for i in range(10) if i % 2 == 0)
for i in mygenerator:
    print(i)