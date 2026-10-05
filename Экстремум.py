n = int(input())
s = []

while abs(n) < 1000:
    s.append(n)
    n = int(input())
text = input()
if text == 'min':
    a = s.index(min(s))
    print(a, s[a])
elif text == 'max':
    a = s.index(max(s))
    print(a, s[a])