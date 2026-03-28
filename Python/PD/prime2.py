n = int(input("Enter a positive integer: "))

if n <= 1:
    print(f"{n} is not prime")
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(f"{n} is not prime")
            break
    else:
        print(f"{n} is prime")


print('+++++++++++++++++++++++++++++++++++')
t = int(input("Enter how many numbers: "))

for _ in range(t):
    n = int(input("Enter a number: "))

    if n <= 1:
        print(f"{n} is not prime")
        continue

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(f"{n} is not prime")
            break
    else:
        print(f"{n} is prime")
