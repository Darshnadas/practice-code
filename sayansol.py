n = int(input("Enter the height: "))
for i in range(0, n):
    print(' ' * (n - (i+1)), '*' * (2 * i + 1))
