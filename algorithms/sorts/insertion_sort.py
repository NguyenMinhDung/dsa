a = [4,2,3,5,1]

for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]

print(" ".join(str(e) for e in a))