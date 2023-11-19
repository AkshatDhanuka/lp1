bs = [200, 500, 300, 400, 600]
ps = [54, 235, 430, 200]

def first_fit(bs, ps):
    allocation = []

    for i in ps:
        for j in range(len(bs)):
            if bs[j] >= i:
                allocation.append(j+1)
                bs[j] -= i
                break
        else:
            print("Not Allocated")
    
    return allocation


def best_fit(bs, ps):
    allocation = []

    for i in ps:
        available_blocks = [x for x in bs if x >= i]
        
        if not available_blocks:
            print("Not Allocated")
            continue

        min_block = min(available_blocks)
        index = bs.index(min_block)
        allocation.append(index+1)
        bs[index] -= i
    
    return allocation

def worst_fit(bs, ps):
    allocation = []

    for i in ps:
        a = max(bs)
        if a >= i:       
            index = bs.index(a)
            allocation.append(index+1)
            bs[index] -= i
        else:
            allocation.append('Not Allocated')

    return allocation    

def next_fit(bs, ps):
    allocation = []
    curr = 0

    for i in ps:
        flag = False
        for j in range(curr, len(bs)):
            if bs[j] >= i:
                allocation.append(j+1)
                bs[j] -= i
                curr = j
                flag = True
                break
        if flag == False:
            allocation.append("Not Allocated")

    return allocation


# print(first_fit(bs, ps)) #Works Properly
# print(best_fit(bs, ps))  #Works Properly
# print(worst_fit(bs, ps)) #Works Properly
print(next_fit(bs, ps))