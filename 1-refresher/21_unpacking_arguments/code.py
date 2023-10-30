def add(x, y):
    return x + y


print(add(5, 7))

add_fun = lambda x, y: x + y
print(add_fun(5, 7))
print((lambda x, y: x + y)(5, 7))  # Not recommended


def double(x):
    return x * 2


s = [1, 2, 3, 4, 5]
doubled = [double(x) for x in s]
print(s)
print(doubled)
print(list(map(double, s)))

# using lambda

s = [1, 2, 3, 4, 5]
doubled = [(lambda x: x * 2)(x) for x in s]
print(s)
print(doubled)
print(list(map(lambda x: x * 2, s)))
