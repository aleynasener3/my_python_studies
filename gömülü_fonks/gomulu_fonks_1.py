from functools import reduce

def double(x):
    return x*2
print(list(map(double,[1,2,3,4])))

print(list(map(lambda x : x**2, (1,2,3,4,5))))

liste1=[1,2,3,4]
liste2=[5,6,7,8]
print(list(map(lambda x,y : x*y,liste1,liste2)))

print(reduce(lambda x,y : x*y, [1,2,3,4]))

def maksimum(x,y):
    if(x>y):
        return x
    else:
        return y

print(maksimum(3,7))

print(reduce(maksimum,[2,5,-1,39]))

print(list(filter(lambda x : x%2==0,[1,2,3,4,5])))

def asal(x):
    i=2
    if(x==1):
        return False
    elif(x==3):
        return True
    else:
        while(i<x):
            if(x%i==0):
                return False
            i+=1
        return True

print(list(filter(asal,range(1,100))))

liste3 = ["a","b","c","d"]

print(list(zip(liste1,liste2,liste3)))

print(list(enumerate(liste3)))

for i,j in enumerate(liste3):
    print(i,j)
