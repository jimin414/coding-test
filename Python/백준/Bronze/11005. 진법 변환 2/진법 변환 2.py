N, B = map(int, input().split())
digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = ""

while N > 0:
    remainder = N % B
    result = digits[remainder] + result
    N //= B

if result == "":
    result = "0"

print(result)

