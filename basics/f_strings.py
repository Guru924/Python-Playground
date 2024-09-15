# used for string formatting

letter = "Hey my name is {} and I am from {}"
country = "India"
name = "Guru"
print(letter.format(name, country))
print(letter.format(country, name))
letter = "Hey my name is {1} and I am from {0}"
print(letter.format(country, name))

# f-string
print(f"Hey my name is {name} and I am from {country}")


txt = "for only {price:.2f} dollars!"
print(txt.format(price = 49.09999))