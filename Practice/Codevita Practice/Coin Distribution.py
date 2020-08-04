def prints(a):
    print(sum(a), a[0], a[1], a[2])
    print()

n = int(input())
l = [[0,0,1],[0,0,2],[0,1,1],[0,1,2],[0,2,1],[0,2,2],[0,3,1],[0,3,2],[1,1,2],[1,2,1]]
if n < 10:
    prints(l[n - 1])
else:
    ans = [0,0,0]
    if n % 10 == 0:
        temp = (n - 10) // 5
        ans = l[9]
        ans[0] += temp
    elif n % 10 < 5:
        temp = (n - (n % 10) - 5) // 5
        ans = l[n%10+5-1]
        ans[0] += temp
    else:
        temp = (n - (n % 10)) // 5
        ans = l[n%10-1]
        ans[0] += temp
    prints(ans)
