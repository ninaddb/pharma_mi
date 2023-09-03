#wap to test if given no is even or odd
n = int(input('Enter a no. '))

if n==0:
    print('It is zero')
elif n % 2 == 0:
    print(n, 'is even')
else:
    print(n, 'is odd')