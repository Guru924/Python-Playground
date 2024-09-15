s = {2, 4, 2, 6}
print(s)
print(type(s))

info = {"carla", 19, False, 5.9, 19}
print(info)
print(type(info))

# for empty set
guru = set()
print(type(guru))

for i in info:
    print(i)


# methods
s1 = {1,2,5,6}
s2 = {3,6,7}
print(s1.union(s2))
# s1.update(s2)
# print(s1,s2)

print(s1.intersection(s2))
# s1.intersection_update(s2)
# print(s1)

#explore more methods