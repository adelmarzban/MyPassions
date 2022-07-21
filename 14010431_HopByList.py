#### Hope Game by Applying LIST ######
Adad = int(100)
a = [*range(1, Adad)]
for i in range(0, len(a)):
    if a[i] % 3 == 0 and a[i] % 5 == 0:
        a[i] = "Hope Hip"
    elif a[i] % 5 == 0:
        a[i] = "hope"
    elif a[i] % 3 == 0:
        a[i] = "hip"
print(a)
