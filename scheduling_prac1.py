at = [0, 1, 2, 3]
bt = [21, 5, 4, 2]

def fcfs(at, bt):
    wt = []
    tt = []
    n = len(at)
    curr = 0

    for i in range(n):
        a = min(at)
        curr += a

        wt.append(curr-at[i])
        curr += bt[i]
        tt.append(wt[i] + bt[i])
    
    print("Waiting time is ", wt)
    print("Turnaround time is ", tt)

def rotate_right(arr):
    n = len(arr)

    temp = arr[0]
    for i in range(1, n):
        arr[i-1] = arr[i]
    arr[n-1] = temp

    return arr 


def rr(at, bt):
    print(bt[0])
    tq = 2
    ct = bt
    n= len(at)
    curr = 0
    wt = [0]*n
    tt = [0]*n
    nr = 0

    while(sum(ct) != 0):
        if ct[0] == 0:
            ct = rotate_right(ct)
            nr += 1
        elif ct[0] <= tq:
            curr += ct[0]
            ct[0] = 0
            index = nr%4
            wt[index] = curr - at[index] -bt[index]
            tt[index] = wt[index] + bt[index]
            ct = rotate_right(ct)
            nr += 1
        else:
            ct[0] -= 2
            curr += 2
            ct = rotate_right(ct)
            nr += 1
    print(wt)
    print(tt)
    

fcfs(at, bt)
rr(at, bt)