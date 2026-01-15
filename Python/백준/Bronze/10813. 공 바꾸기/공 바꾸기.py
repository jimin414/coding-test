N, M = map(int, input().split())
num = list(range(1, N+1))
for _ in range(M):
     i,j = map(int, input().split())
     t = num[i-1]
     num[i-1] = num[j-1]
     num[j-1] = t
for i in range(N):
    print(num[i], end = ' ')