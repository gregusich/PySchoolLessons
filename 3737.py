def rg(c, s1, k, n, s2):
    c = input()
    k = len(c) // 2 + 1
    s1 = c[0:k]
    s1 = s1.reverse()
    s2 = c[k:]
    s2 = s2.reverse()
    n = s1 + s2
    print(n)


rg(s1=str, c=str, k=int, s2=str, n=str)
