# 3831
def biggers(s, s1):
    s = list(map(int, input().split()))
    s1 = s
    for i in range(len(s)):
        if i + 1 != len(s):
            if s[i + 1] > s[i]:
                print(s[i + 1], end=" ")
        else:
            break


biggers(s=str, s1=str)
