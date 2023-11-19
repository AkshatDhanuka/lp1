# def bestfit(bs, ps):
#     allocation = []
    
#     for i in ps:
#         res = min(x for x in bs if x >= i)
#         index = bs.index(res)
#         allocation.append(index+1)
#         bs[index] -= i
        
#     print(allocation)
#     return allocation

# bs = [100, 500, 200, 300, 600]
# ps = [212, 417, 112, 426]

# bestfit(bs, ps)


# def worstfit(bs, ps):
#     allocation = []
    
#     for i in ps:
#         res = max(bs)
#         if(res >= i):
#             index = bs.index(res)
#             allocation.append(index+1)
#             bs[index] -= i
#         else:
#             print("Not Allocated")

#     return allocation

# bs = [100, 500, 200, 300, 600]
# ps = [212, 417, 112, 426]


# print(worstfit(bs, ps))
# print(bs)

# def firstfit(bs, ps):
#     allocation = []
    
#     for i in ps:
#         flag = True
#         for j in range(1, len(bs)):
#             if bs[j] >= i:
#                 allocation.append(j+1)
#                 bs[j] -= i
#                 flag = False
#                 break
#         if flag == True:
#             allocation.append("Not allocated")
        
#     return allocation

# bs = [100, 500, 200, 300, 600]
# ps = [212, 417, 112, 426]

# print(firstfit(bs, ps))


def nextfit(bs, ps):
    allocation = []
    
    curr = 0
    for i in range(len(ps)):
        for j in range(curr, len(bs)):
            if  bs[j] >= ps[i]:
                allocation.append(j+1)
                bs[j] -= ps[i]
                curr = j
                break
        else:
            allocation.append("Not Allocated")
    
    return allocation 

bs = [100, 500, 200, 450, 600]
ps = [212, 417, 112, 426]

print(nextfit(bs, ps))
