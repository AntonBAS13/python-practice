n = int(input())
alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
base = 36
s = ''

if n == 0:
    print(n)
else:
    while n > 0:
        s = alphabet[n % 36] + s
        n //= base
    print(s)