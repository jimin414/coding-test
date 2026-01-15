N, M = map(int, input().split())
basket = list(range(1, N+1))
temp = 0
for x in range(M):
    i, j = map(int, input().split())
    temp  = basket[i-1:j]
    temp.reverse()
    basket[i-1:j] = temp
for x in range(N):
    print(basket[x], end=" ")
