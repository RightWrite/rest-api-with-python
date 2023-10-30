# def print(name: str):
#     print("hello")
#
#
# print("hello")


friends = ["Rolf", "Bob"]


def add_friends():
    friend_name = input("Enter your frined's name")
    # friends = friends + friend_name # this won't work
    f = friends + [friend_name]
    print(f)


add_friends()


