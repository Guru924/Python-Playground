marks = [12, 35, 23, 97, 63]

# index = 0
# for mark in marks:
#     print(mark)
#     if(index == 2):
#         print("Guru you fail!! xd....")
#     index += 1

for index, mark in enumerate(marks, start=1):
    print(mark)
    if(index == 3):
        print("Guru you fail!! xd....")