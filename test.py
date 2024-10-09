d = ['']
def input():
    try:
        out = d[0]
        d.pop(0)
    except:
        raise Exception("Incomplete Inputs")

    return out 

for i in range(3):
    print(i)