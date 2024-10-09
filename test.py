d = ['13']
def input():
    try:
        out = d[0]
        d.pop(0)
    except:
        raise Exception("Incomplete Inputs")

    return out 

# Check if number is Prime or Not
# Take input from the user
n = int(input())

# Check if the number is prime
prime = True
if n <= 1:
    prime = False
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            prime = False
            break

if (prime):
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")