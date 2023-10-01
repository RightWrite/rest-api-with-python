numbers = [1, 3, 5]
doubled = [x * 2 for x in numbers]
print(doubled)

friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
starts_s = [f for f in friends if f.startswith("S")]
print(starts_s)

print("friends: ", id(friends), "starts_s: ", id(starts_s))