def ans(a, b):
    cnt = a.count('*')
    if cnt == 1:
        return "A"
    elif cnt == 2:
        return "U"
    elif cnt == 3:
        cnt2 = b.count('*')
        if cnt2 == 1:
            return "I"
        elif cnt2 == 2:
            return "O"
        elif cnt2 == 3:
            return "E"

def ans2(a, b):
    i = 0
    t = []
    t1=[]
    while i < len(a):
        t.append(a[i:i+3])
        t1.append(b[i:i+3])
        i += 3
    ret = ""
    for i in range(len(t)):
        ret += ans(t[i], t1[i])
    return ret

def ans3(a, b, c):
    x = []
    y=[]
    z=[]
    for i in range(len(a)):
        p = ""
        q = ""
        r = ""
        for j in range(len(a[i])):
            if a[i][j] == b[i][j] and b[i][j] == c[i][j] and c[i][j] == ".":
                pass
            else:
                p += a[i][j]
                q += b[i][j]
                r += c[i][j]
        x.append(p)
        y.append(q)
        z.append(r)
        x = [i for i in x if len(i)]
        y= [i for i in y if len(i)]
        z = [i for i in z if len(i)]
    return x, y, z


def solve(a, b):
    st = ""
    for i in range(len(a)):
        if len(a[i]) > 3:
            st += ans2(a[i], b[i])
        elif len(a[i]) == 0:
            pass
        elif len(a[i]) != 0:
            st += ans(a[i], b[i])
        st += "#"
    return st[:-1]

n = int(input())
s1 = input().replace(' ','').split('#')
s2 = input().replace(' ','').split('#')
s3 = input().replace(' ','').split('#')
s1, s2, s3 = ans3(s1, s2, s3)
print(solve(s1, s2))
