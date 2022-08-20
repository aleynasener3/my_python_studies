liste = [1,2,3,4,5]

def test(x):
    if (x%2==0):
            return x
        else:
            raise ValueError
        
for x in liste:
    try:
        print(test(x))

    except ValueError:
        pass
        
