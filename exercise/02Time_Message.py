import time
timestamp = time.strftime('%H: %M: %S')
print(timestamp)

hour = int(time.strftime('%H'))
print(hour)

name = input("Enter your name\n")

if(hour > 0 and hour < 12):
    print("Good Morning "+name+"!")
elif(hour >= 12 and hour < 17):
    print("Good Afternonn "+name+"!")
elif(hour >= 17 and hour < 21):
    print("Good Evening "+name+"!")
else:
    print("Good Night "+name+"!")