def reverse(s):
    if(type(s) != str):
        raise ValueError("please write str")
    else:
        return s[::-1]


print(reverse("python"))
