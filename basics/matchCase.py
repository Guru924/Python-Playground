x = int(input("Enter a number from 1 to 10: "))

match x:
    case 0:
        print("x is zero")
    case 1: 
        print("case is 1")
    case 2:
        print("case is 2")
    case 3: 
        print("case is 3")
    case 4:
        print("case is 4")
    case 5: 
        print("case is 5")
    case 6:
        print("case is 6")
    case 7: 
        print("case is 7")
    case 8: 
        print("case is 8")
    case 9: 
        print("case is 9")
    case _ if x > 10:
        print(x,"is greater than 10")
    case _:
        print(x,"invalid number")