def add(a):
    if (a[0] == "SHIRT" or a[0] == "SHOE") and (int(a[1]) > 0) and dt[a[0]] == 0:
        dt[a[0]] += int(a[1])
        return a[1]
    else:
        return -1
    
def remove(a):
    if a[0] == "SHIRT" or a[0] == "SHOE":
        dt[a[0]] = -1
        return 1
    else:
        return -1
        
def getqty(a):
    if dt[a[0]] == -1:
        return 0
    return dt[a[0]]

def inc(a):
    if (a[0] == "SHIRT" or a[0] == "SHOE") and (int(a[1]) > 0) and dt[a[0]] != 0 and dt[a[0]] != -1:
        dt[a[0]] += int(a[1])
        return a[1]
    else:
        return -1

def dec(a):
    if (a[0] == "SHIRT" or a[0] == "SHOE") and (int(a[1]) > 0) and dt[a[0]] != 0 and dt[a[0]] != -1:
        dt[a[0]] -= int(a[1])
        if dt[a[0]] == 0:
            dt[a[0]] = -1
        return a[1]
    else:
        return -1

def setcost(a):
    if (a[0] == "SHIRT" or a[0] == "SHOE") and float(a[1]) > 0:
        qw = float(a[1])
        qw = round(qw, 1)
        pr[a[0]] = qw
        return qw
    else:
        return -1
        
def addc(a):
    if (a[0] == "SHIRT" or a[0] == "SHOE") and (int(a[1]) > 0) and ct[a[0]] == 0:
        ct[a[0]] += int(a[1])
        return a[1]
    else:
        return -1
        
def removec(a):
    if a[0] == "SHIRT" or a[0] == "SHOE":
        ct[a[0]] = -1
        return -1
    else:
        return 1


def incc(a):
    if (a[0] == "SHIRT" or a[0] == "SHOE") and (int(a[1]) > 0) and ct[a[0]] != 0 and ct[a[0]] != -1:
        ct[a[0]] += int(a[1])
        return a[1]
    else:
        return -1

def decc(a):
    if (a[0] == "SHIRT" or a[0] == "SHOE") and (int(a[1]) > 0) and ct[a[0]] != 0 and ct[a[0]] != -1:
        ct[a[0]] -= int(a[1])
        if ct[a[0]] == 0:
            ct[a[0]] = -1
        return a[1]
    else:
        return -1

def order(a):
    total = 0
    for k, v in ct.items():
        total += (v * pr[k])
    ret = "{0:.2f}".format(total)
    return ret

def solve(l):
    if l[0] == "SM":
        if l[1] == "ADD":
            print(add(l[2:]))
        elif l[1] == "GET_QTY":
            print(getqty(l[2:]))
        elif l[1] == "REMOVE":
            print(remove(l[2:]))
        elif l[1] == "INCR":
            print(inc(l[2:]))
        elif l[1] == "DCR":
            print(dec(l[2:]))
        elif l[1] == "SET_COST":
            print(setcost(l[2:]))
        
    elif l[0]=="S":
        if l[1] == "ADD":
            print(addc(l[2:]))
        elif l[1] == "REMOVE":
            print(removec(l[2:]))
        elif l[1] == "INCR":
            print(incc(l[2:]))
        elif l[1] == "DCR":
            print(decc(l[2:]))
        elif l[1] == "GET_ORDER_AMOUNT":
            print(order(l[2:]))



from collections import defaultdict

dt = defaultdict(int)
pr=defaultdict(float)
ct=defaultdict(int)

for i in range(int(input())):
    while True:
        l = input().split()
        if l[0] == 'END':
            break
        else:
            if l[0] == "CMD":
                solve(l[1:])
    dt.clear()
    pr.clear()
    ct.clear()
