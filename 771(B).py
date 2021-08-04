#https://codeforces.com/contest/711/problem/B
#https://codeforces.com/contest/711/submission/20306590

def main():
    n = int(input())
    print(f"intput : {n}")
    if n == 1:
        print(1)
        return
    l = list(list(map(int, input().split())) for _ in range(n))
    print(f"list(list(map(int, input().split())) for _ in range(n)) IS : {l}")
    '''
    Sample I/O
   I: l = list(list(map(int, input().split())) for _ in range(2))
      45 45 74
      12 41 6
   O: >>> l
      [[45, 45, 74], [12, 41, 6]]
    
    '''
    
    for i, r in enumerate(l, -1):
        if 0 in r:
            break
        print(f"The enumerate in l (i and r) is : {i},{r}")    
    '''
    l =[[4,0,2],[3,5,7],[8,1,6]]
    
    >>> for i,r in enumerate(l,-1):
	           print(i,r)

    >>> -1 [4, 0, 2]
         0 [3, 5, 7]
         1 [8, 1, 6]
    '''
    
    s = sum(l[i])
    print(f"s = sum is :== {s}")
    x = s - sum(r)
    print(f"x = s - sump(r) is :== {x}")
    print(f"sum(r) is :== {sum(r)}")
    print("The r in Sum(r) is from enumerate(l,-1)")
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
