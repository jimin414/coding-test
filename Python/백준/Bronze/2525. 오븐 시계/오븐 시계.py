A, B = map(int, input().split())
C = int(input())

if (B+C)<60:
    print(A, B+C)
else:
    A += (B+C)//60
    if A>23:
        A-=24
    D = (B+C)%60
    print(A, D)