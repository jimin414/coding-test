import math

A, B, V = map(int, input().split())

days = (V - A) / (A - B) + 1
print(math.ceil(days))
