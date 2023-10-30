friend_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}
print(friend_ages["Rolf"])

for friend in friend_ages:
    print(f"{friend} is {friend_ages[friend]} old")

for friend,age in friend_ages.items():
    print(f"{friend} is {age} old")

friend_ages["Bob"] = 20
print(friend_ages)

friends = [
    {"name": "Rolf", "age": 24},
    {"name": "Adam", "age": 30}
]

print(friends)
print(friends[0])
