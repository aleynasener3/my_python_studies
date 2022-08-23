import sys

print(dir(sys))

sys.exit()#altındaki hiçbir kod çalışmıyor

sys.stderr.write("hata mesaji")

sys.stderr.flush()

sys.stdout.write("normal yazi")

print(sys.argv)

for i in sys.argv:
    print(i)
