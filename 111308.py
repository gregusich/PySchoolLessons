# 111308
def ispalidrome(s):
    s = input()
    s = s.lower()
    if s == s[::-1]:
        print("YES")
    else:
        print("NO")


ispalidrome(s=str)
