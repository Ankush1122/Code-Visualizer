d = ['2\r', '3']
def input():
    try:
        out = d[0]
        d.pop(0)
    except:
        raise Exception("Incomplete Inputs")

    return out 

a = int(input())
b = int(input())

print(a+b)

x = -1
for i in range(3):
    if (i % 3 == 0):
        x = 0
    elif (i % 3 == 1):
        x = 1
    else:
        x = 2
    print(x)