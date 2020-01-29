n=5
for i in range(n,0,-1):
    for j in range(n,0,-1):
        if (j>i):
            print(" ",end='')
        else:
            print(chr(65+j-1),end=' ')
    print()