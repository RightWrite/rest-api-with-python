name = "Bob"
greeting = f"Hello, Bob"
print(greeting)

name = "Rolf"
print(greeting)

greeting = f"Hello, {name}" # defines greeting as "Hello, Rolf" while creating a new variable
print(greeting)

name = "Gunnar"
print(greeting) # still prints "Hello, Rolf" because the value of greeting is set to "Hello, Rolf"

new_greeting = "Hello, {}"
print(new_greeting.format(name)) # prints "Hello, Gunnar" because the value of name is set to "Gunnar"

name = "Bob"
print(new_greeting.format(name)) # prints "Hello, Bob" because the value of name is set to "Bob"