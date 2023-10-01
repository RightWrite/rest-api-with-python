def add(x, y=0):
    print(x + y)


add(1, 2)
add(8)

default_y=1
def add_new(x, y=default_y):
    print(x + y)


add(1, 2)
add(8)

default_y=3 # This has no effect as function add_nw is already initialized with default_y=1
add(8)