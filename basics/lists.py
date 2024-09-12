marks = [3,5,6]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])

# we can change or alter the list

list1 = [3,4,5, "Guru", True,5]
print(list1)
print(list1[-3]) #len(list1) = 5, 5-3 = 2(index)
print(list1[2])

if 7 in marks: 
    print("Yes")
else:
    print("No")

if "Guru" in list1: 
    print("Yes")
else:
    print("No")

# same thing applies for strings as well!
# if "uru" in "Guru":
#     print("Yes!!!")    

print(list1[:])
print(list1[1:-1])

#jump index
print(list1[1:4:2])

# list comprehension
# lst = [i for i in range(4)]
# print(lst)

lst1 = [i for i in range(10) if i%2 ==0]
print(lst1)

print(list1.count(5))

