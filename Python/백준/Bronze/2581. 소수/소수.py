import math

M = int(input())
N = int(input())

primes = []

for num in range(M, N+1):
    if num < 2:
        continue
    is_prime = True
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)

if len(primes) == 0:
    print(-1)
else:
    print(sum(primes))
    print(min(primes))
