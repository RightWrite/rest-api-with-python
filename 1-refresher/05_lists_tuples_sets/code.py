l = ["Bob", "Rolf", "Anne"]
t = ("Bob", "Rolf", "Anne")
s = {"Bob", "Rolf", "Anne"}
print(l[0])
print(t[0])
# print(s[0]) # sets are unordered, so this will not work
l[0] = "Smith"
print(l)
# t[0] = "Smith" # tuples are immutable, so this will not work
# print(t)
# s[0] = "Smith" # sets are unordered, so this will not work
# print(s)
l.append("Jen")
print(l)
# t.append("Jen") # tuples are immutable, so this will not work
# print(t)
s.add("Jen")



# t.remove("Bob") # tuples are immutable, so this will not work
# print(t)
s.remove("Bob")
print(s)


single_value_tuple = ("Bob",)
print(single_value_tuple)
single_value_tuple_one = "10",
print(single_value_tuple_one)
