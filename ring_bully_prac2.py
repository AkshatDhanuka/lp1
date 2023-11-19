state = [True, True, True, True, True]
n = len(state)

def down(pno, state):
    if (pno<1) or (pno>n):
        print("Invalid Process Number")
        return

    if state[pno-1] == False:
        print("The Process is already down")
        return
    else:
        state[pno-1] = False
    
def up(pno, state):
    if (pno<1) or (pno>n):
        print("Invalid Process Number")
        return

    if state[pno-1] == True:
        print("The Process is already up")
        return
    else:
        state[pno-1] = True

# print(state)
down(2, state)
down(5, state)
# print(state)

def bully(pno, state):
    if (pno<1) or (pno>n):
        print("Invalid Process Number")
        return

    if state[pno-1] == False:
        print("The Process is already down")
        return

    print(f"Election is started by the process p{pno}")

    for i in range(pno+1, n+1):
        print(f"Election message sent from p{pno} to p{i}")
    
    # print(pno)
    # print(n)
    # print(state)
    for i in range(pno, n):
        if state[i] == True:
            print(f"OK message sent from p{i+1} to p{pno}")
    
    ans = 0
    for i in range(n):
        if state[i] == True:
            var = i
        ans = max(ans, var)
    
    print(f"Process {ans+1} informs everyone that it is the winner")

def ring(pno, state):
    if (pno<1) or (pno>n):
        print("Invalid Process Number")
        return

    if state[pno-1] == False:
        print("The Process is already down")
        return

    print(f"Election is started by the process p{pno}")

    if(pno == 1):
        just = pno
        while(pno!=n+1):
            if state[pno-1] == True:
                print(f"Election message sent from p{just} to p{pno}")
                just = pno
            pno += 1
    else:
        start = pno
        while(pno!=n+1):
            if state[pno-1] == True:
                print(f"Election message sent from p{start} to p{pno}")
                just = pno
            pno+=1
        pno = 1
        while(pno != start):
            if state[pno-1] == True:
                print(f"Election message sent from p{just} to p{pno}")
                just = pno-1
            pno += 1
                

    ans = 0
    for i in range(n):
        if state[i] == True:
            var = i
        ans = max(ans, var)    
    print(f"Process {ans+1} informs everyone that it is the winner")
        

bully(1, state)
ring(3, state)