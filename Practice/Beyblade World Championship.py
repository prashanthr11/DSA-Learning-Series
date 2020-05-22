def solve():
    n = int(input())
    cnt = 0
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a = sorted(a, reverse = True)
    b = sorted(b, reverse = True)
    for i in range(len(b)):
        for j in a:
            if b[i] < j:
                cnt += 1
                a.remove(j)
            else:
                a.remove(min(a))
            break
    print(cnt)
    
def main():
    t = int(input())
    for i in range(t):
        solve()

main()
