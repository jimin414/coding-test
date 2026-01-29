A = []
for _ in range(9):
    a = list(map(int, input().split()))
    A.append(a)

MAX = max(max(row) for row in A)
print(MAX)
for r in range(len(A)):
    for c in range(len(A[r])):
        if A[r][c] == MAX:
            print(r+1, c+1)
