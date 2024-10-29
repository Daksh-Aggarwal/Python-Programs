num = int(input("Enter the number: "))
primes = []

for i in range(2, num + 1):
    isPrime = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            isPrime = False
            break

    if isPrime:
        primes.append(i)

print(primes)