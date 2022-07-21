#### Simple Hope Game ######

Adad = int(100)
for i in range(1, Adad + 1):
    if i % 5 == 0 and i % 3 == 0:
        i = "Hope Hip"
    elif i % 5 == 0:
        i = "Hope"
    elif i % 3 == 0:
        i = "Hip"
    print(i)
