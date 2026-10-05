n = int(input())
flag = True

if n == 1:
    print('НЕТ')
else:
    for i in range(2, n - 1):
        if n % i == 0:
            flag = False
            print('НЕТ')
            break
    if flag is True:
        print('Простое')

        
  