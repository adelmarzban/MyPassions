#### Hope Game by Applying LIST ######
a = [*range(1, 101)]
for i in range(0, len(a)):
    if a[i] % 3 == 0 and a[i] % 5 == 0:
        a[i] = "Hope Hip"
    elif a[i] % 5 == 0:
        a[i] = "hope"
    elif a[i] % 3 == 0:
        a[i] = "hip"
print(a)
