def multiple(*args):
    result = 1
    for x in args:
        result = result * x
    return result


result = multiple(1, 2, 3)
print(result)


def add(x, y):
    return x + y


n = [1, 2]
print(add(*n))

d = {"x": 3, "y": 5}
print(add(**d))

def calculate(*args,operator):
    print(args)
    if operator=="+":
        return add(*args)
    if operator=="*":
        return multiple(*args)

print(calculate(1,2,operator="+"))
print(calculate(1,2,operator="*"))