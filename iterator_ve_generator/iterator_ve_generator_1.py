
liste=[1,2,3,4]

iterator = iter(liste)

while True:
    try:
        print(next(iterator))

    except StopIteration:
        break
