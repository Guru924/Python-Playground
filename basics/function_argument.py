# def average(a, b):
#     print("The average is:",(a+b)/2)

# average(4,6)

# default argument
def average(a = 9, b=1):
    print("The average is:",(a+b)/2)

average()

# keyword argument
average(b = 3, a = 5)

# variable-length-argument
# This way the function will receive a tuple of arguments, and can access the items accordingly:
def avg(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    print("avg is:",sum/len(numbers))

avg(1,2,3,4)

def name(**name):
    print(type(name))

    # print('Hello', name['fname'], name['mname'], name['lname'])
    return ('Hello'+" "+ name['fname'] +" "+ name['mname'] +" "+ name['lname'])

msg = name(mname = "Prasad", fname = "Guru", lname = 'Das')
print(msg, type(msg))
