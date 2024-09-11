# i = 0
# while i < 3:
#     print(i)
#     i = i + 1

# i = 1
# while i < 6:
#   print(i)
#   i += 1
# else:
#   print("i is no longer less than 6")

# break and continue

# i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     break
#   i += 1
# else:
#   print("i is no longer less than 6")

# i = 1
# while i < 6:
#   i += 1
#   if i == 4:
#     continue
#   print(i)
# else:
#   print("i is no longer less than 6")

# do while emulate

i = 0
while True:
    print(i)
    i = i+1
    if i%100 == 0:
        break