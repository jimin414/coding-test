A = [input() for _ in range(5)]

max_len = max(len(w) for w in A)

result = ""
for i in range (max_len):
    for w in A:
        if i < len(w):
            result += w[i]
print(result)