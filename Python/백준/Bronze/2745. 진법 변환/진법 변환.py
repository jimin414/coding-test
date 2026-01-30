N, B = input().split()
B = int(B)

result = 0
length = len(N)

for i in range(length):
    char = N[length - 1 - i]  # 오른쪽 끝부터 처리
    if char.isdigit():
        value = int(char)
    else:
        value = ord(char) - ord('A') + 10
    result += value * (B ** i)

print(result)
