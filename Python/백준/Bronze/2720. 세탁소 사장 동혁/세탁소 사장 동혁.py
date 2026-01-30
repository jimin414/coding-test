T = int(input())
for _ in range(T):
    n = int(input())
    quarters = n // 25
    n %= 25
    dimes = n // 10
    n %= 10
    nickels = n // 5
    n %= 5
    pennies = n
    print(quarters, dimes, nickels, pennies)
