import sys
input()
s=sys.stdin.read()
x=s.find('OO')
print('NO' if x<0 else 'YES\n'+s[:x]+'++'+s[x+2:])

==========

def main():
    n = int(input())
    if n == 1:
        print(1)
        return
    l = list(list(map(int, input().split())) for _ in range(n))
    for i, r in enumerate(l, -1):
        if 0 in r:
            break
    s = sum(l[i])
    x = s - sum(r)
    if x <= 0:
        x = -1
    r[r.index(0)] = x
    if (any(sum(r) != s for r in l) or
            any(sum(r) != s for r in zip(*l)) or
                sum(l[i][i] for i in range(n)) != s or
                sum(l[i][j] for i, j in enumerate(range(n - 1, -1, -1))) != s):
        x = -1
    print(x)
 
 
if __name__ == '__main__':
    main()
