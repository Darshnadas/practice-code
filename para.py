n = int(input("Enter the desired height: "))
for i in range(0,n):
    for j in range(0,n):
        if(i == 0 or j == 0 or i == j or i == n-1 or j == n-1 or i + j == n-1):
            print('*',end="")
        else:
            print(" ",end ="")
    print("")                     