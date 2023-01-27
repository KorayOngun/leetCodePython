ways = [[0,1,5],[0,2,6],[0,3,1],[3,2,2],[2,1,1],[1,5,1],[5,6,2],[2,4,4],[5,4,3],[4,6,5]]
#a0 b1 c2 e3 d4 f5 h6
src = 0
dst = 6
# en kısa yol 
n = 7 
w = 10
cost = [float("inf")] * n
cost[src] = 0
print(cost)
for t in range(w):
    tempCost = cost.copy()
    for s,d,p in ways:
        if tempCost[s] == float("inf"):
            continue
        elif tempCost[s] + p <= tempCost[d]:
            tempCost[d] = tempCost[s] + p
    cost = tempCost
    
print(cost[dst])