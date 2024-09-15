def func1():
    a = input("Enter the number: ")
    print(f"Multiplication table of {a} is: ")
    try:
        for i in range(1,11):
         print(f"{a} X {i} = {int(a)*i}")
        return 1
    except Exception as e:
        print(e)
        return 0
    finally:
        print("some imp lines of code")
        print("End of program")

x = func1()
print(x)