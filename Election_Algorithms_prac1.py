# state = [True, True, True, True, True]
# n = len(state)

# def down(pno, state):
#     if state[pno-1] == False:
#         print("Process is already down")
#     else:
#         state[pno-1] = False

# def up(pno, state):
#     if state[pno-1] == True:
#         print("Process is already up")
#     else:
#         state[pno-1] = True

# down(2, state)
# down(5, state)

# # Testing the Up and Down Function
# # down(2, state)
# # down(5, state)
# # print(state)
# # up(2, state)
# # print(state)


# def bully(pno, state):
#     if (pno > n) or (pno < 1):
#         print("Invalid Process Id")
#         return
    
#     if state[pno-1] == False:
#         print("The process is down and hence cannot start election")

#     if pno == n:
#         print("The process has the highest priority and hence will not send any message to the higher Priority and hence will be the coordinator by default")
#         return

#     print("Election is started by the process ", pno)

#     for i in range(pno, n):
#         print("Election message is sent from the process ", pno, "to the process ", i+1)
    
#     for i in range(pno, n):
#         if state[i] == True:
#             print("OK message is sent from the process ", i+1, "to the process ", pno)
    
#     for i in range(pno, n):
#         if state[i] == True:
#             bully(i + 1, state)
#             return

#     winner = pno 
     
#     for i in range(n):
#         if (state[i] == True) and (i + 1 > winner):
#             winner = i + 1

    
#     print("Election is won by the process ", winner)
#     print("Process ", winner, "informs everyone that the new coordinator is ", winner)

# bully(1, state)
        



# RING ELECTION ALGORITHM

state = [True, True, True, True, True]
n = len(state)

def down(pno, state):
    if state[pno-1] == False:
        print("Process is already down")
        return
    else:
        state[pno-1] = False

def up(pno , state):
    if state[pno-1] == True:
        print("Process is already up")
        return
    else:
        state[pno-1] == True

def ring(pno, state):
    if (pno < 1) or (pno > n):
        print("Invalid Process ")
        return

    if state[pno] == False:
        print("The process is down and hence cannot start the Election")

    start = pno-1
    curr = (start+1)%n
    prev = start

    while curr != start:
        if state[curr] == True:
            print("p", prev+1, " sends election message to ", curr+1)
            prev = curr
        
        curr = (curr+1)%n

    print("p", prev+1, "sends election message to ", curr+1)
    
    winner = pno 
     
    for i in range(n):
        if (state[i] == True) and (i + 1 > winner):
            winner = i + 1

    print("Election is won by the process ", winner)
    print("Process ", winner, "informs everyone that the new coordinator is ", winner)

down(2, state)
down(5, state)
ring(1, state)    
