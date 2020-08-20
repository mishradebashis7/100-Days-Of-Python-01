#MemorizationTechnique
val = [60, 100, 120] 
wt = [10, 20, 30] 
W = 50
n = len(val) 
t = [[-1 for i in range(W + 1)] for j in range(n + 1)] 
def knapsack(wt, val, W, n):	 
	if n == 0 or W == 0: 
		return 0
	if t[n][W] != -1: 
		return t[n][W] 
	if wt[n-1] <= W: 
		t[n][W] = max( 
val[n-1] + knapsack( 
wt, val, W-wt[n-1], n-1), 
knapsack(wt, val, W, n-1)) 
		return t[n][W] 
	elif wt[n-1] > W: 
		t[n][W] = knapsack(wt, val, W, n-1) 
		return t[n][W] 
print(knapsack(wt, val, W, n)) 
 