try:
    a = int(input("number 1:"))
    b = int(input("number 2:"))
    print(a/b)

except ValueError:#except (ValueError,ZeroDivisionError )
    print("please write only number")

except ZeroDivisionError:
    print("you cant divide a number to zero")
finally:#her türlü çalışacak kod
    print("code ended")
