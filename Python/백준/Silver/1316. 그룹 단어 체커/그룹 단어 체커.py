N = int(input())
count = N
for i in range (N):
    word = input()
    for s in range(len(word)-1):
        if word[s] == word[s+1]:
            continue
        elif word[s] in word[s+1:]:
            count -= 1
            break
print(count)
