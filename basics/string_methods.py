a = "Guru !!!! Prasad"
print(a)

print(len(a))

print(a.upper()) #new string
print(a.lower())

print(a.rstrip("!"))

print(a.replace("Guru",'Prasad'))

print(a.split(" "))

blogHeading = "introduction tO js. Hello"
print(blogHeading.capitalize())

str1 = "welcome to the console!!!"
print(str1.center(50))
print(len(str1.center(50)))

print(a.count("u"))

print(str1.endswith("!!!"))
print(str1.endswith("to", 4,10))

print(str1.find("to")) # else return -1

print(str1.index('to')) # else return exceptions

print(str1.isalnum())

print(str1.islower())

print(str1.isprintable())

str2 = "     "
print(str2.isspace())

str3 = "World Health Organization"
print(str3.istitle())

print(str3.startswith("World"))

print(str3.swapcase())

print(str1.title())