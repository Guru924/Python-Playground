# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

# Short Hand If
if a > b: print("a is greater than b")
# Short Hand If ... Else
a = 2
b = 330
print("A") if a > b else print("B")
# Ternary Operators
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
print(9) if a>b else ""
c = 9 if a>b else 0
print(c)


a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")


# Nested if
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

# The pass Statement
# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
a = 33
b = 200

if b > a:
  pass