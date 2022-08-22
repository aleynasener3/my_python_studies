def triangle(demet):
    if (demet[0]*demet[0]+demet[1]*demet[1]==demet[2]*demet[2]):
        return True
liste=[(3,4,5),(6,8,10),(3,10,7)]

print(list(filter(triangle,liste)))
