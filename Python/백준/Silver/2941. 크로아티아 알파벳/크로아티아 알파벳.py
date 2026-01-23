word = input()
croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
count = 0
i = 0
while i < len(word):
    if word[i:i + 3] == "dz=":
        count += 1
        i += 3
    elif word[i: i+2] in croatia:
        count += 1
        i+=2
    else:
        count += 1
        i += 1
print(count)