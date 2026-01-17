word = input().upper()
cnt = {}
for c in word:
    if c in cnt:
        cnt[c] += 1
    else:
        cnt[c] = 1
max_cnt = max(cnt.values())
result = []
for c in cnt:
    if cnt[c] == max_cnt:
        result.append(c)
if len(result)==1:
    print(result[0])
else:
    print('?')