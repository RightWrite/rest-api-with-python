x = (5, 11)
a, b = x
print(a)
print(b)
print(x)

people = [("Bob", 42, "Mechanic"), ("James", 24, "Artist"), ("Harry", 32, "Lecturer")]
for name, age, profession in people:
    print(f"Name: {name}, Age: {age}, Profession: {profession}")


numbers = [1, 2, 3, 4, 5]
head, *tail = numbers
print(head)
print(tail)

*other, last = numbers
print(other)
print(last)
