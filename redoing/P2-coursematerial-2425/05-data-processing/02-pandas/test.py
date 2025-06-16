def compose(f, g):
    return lambda x: f(g(x))

square = lambda x: x * x
increment = lambda x: x + 1

new_function = compose(square, increment)

# We can do this because the return value of compose is a function. It's a lambda expression but still a function; that's why we can call the new_function like this.
print(new_function(3))


def testing(f, g):
    def get_value(x):
        return f(g(x))
    return get_value



testing_function = testing(square, increment)
print("testing", testing_function(5))
print(testing(square, increment)(6))

def repeat(num_times):
    def decorator(func):
        # 'num_times' and 'func' are captured by the inner 'wrapper'
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(num_times=3) # This is equivalent to `say_hello = repeat(3)(say_hello)`
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice")


def counter():
    count = 0 # 'count' is captured by the inner function
    def increment():
        nonlocal count # Declare that 'count' is not local to 'increment' but in an enclosing scope
        count += 1
        return count
    return increment

my_counter = counter()
print(my_counter()) # Output: 1
print(my_counter()) # Output: 2
another_counter = counter() # A new independent counter
print(another_counter()) # Output: 1

# 1 2 1 3 2 3 3 4 5
# the order here of execution here is:
# for every y, y + x
# so y(0) + x(0)
# y (0) + x (1)
# ...
# y (1) + x (0)
# y (1) + x (1)
lst = [x + y for x in range(4) for y in range(3) if x != y ]
print(lst)


pairs = [(1, 2), (3, 4), (2, 3), (4, 5)]
pairs_sorted = sorted(pairs, key=lambda x: x[1] - x[0])
print(pairs_sorted)