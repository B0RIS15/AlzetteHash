def rotation(z, n):
    return (((z) >> (n)) | ((z) << (32 - (n))))

def Alzette(x, y, c):
    x += rotation(y, 31)
    y ^= rotation(x, 24)
    x ^= c
    x += rotation(y, 17)
    y ^= rotation(x, 17)
    x ^= c
    x += y
    y ^= rotation(x, 31)
    x ^= c
    x += rotation(y, 24)
    y ^= rotation(x, 16)
    x ^= c
    return x, y

def Alzette_inv(x, y, c):
    x ^= c
    y ^= rotation(x, 16)
    x -= rotation(y, 24)
    x ^= c
    y ^= rotation(x, 31)
    x -= y
    x ^= c
    y ^= rotation(x, 17)
    x -= rotation(y, 17)
    x ^= c
    y ^= rotation(x, 24)
    x -= rotation(y, 31)
    return x, y

x = int(input("Enter x - "))
y = int(input("Enter y - "))
c = int(input("Enter c - "))
rez = Alzette(x, y, c)
print(rez)
x = rez[0]
y = rez[1]
print("===============")
print(Alzette_inv(x, y, c))
