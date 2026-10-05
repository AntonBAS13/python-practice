n = int(input())
a = n * '*'
a1 = f'--{a}--'
print(a1 * n)


for r in reversed(range(1, n, 2)):
    stars = r  
    space = (n - stars) // 2
    flag = '  ' + ' ' * space + '*' * stars + ' ' * space + '  '
    print(flag * n)