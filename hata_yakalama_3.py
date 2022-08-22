def reverse(s):
    if(type(s) != str):
        raise ValueError("please write str") #raise error_name ("note")
    else:
        return s[::-1]


print(reverse("python"))
