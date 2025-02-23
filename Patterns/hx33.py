nr=int(input('Number of rows?:'))
print('Mirror triangle')
for i in range(1,nr+1):
    for j in range(1,nr+1):
        if(j <= nr -i):
            print('', end='  ')
        else:
            print('*', end = '  ')
    print()