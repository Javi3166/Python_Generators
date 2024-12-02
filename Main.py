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

print("\nOnce the list has been iterated through and there is an attempt to iterate further, it generates a StopIteratrion error.")

