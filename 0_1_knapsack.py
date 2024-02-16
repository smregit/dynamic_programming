def knapsack01(arr,capacity):
    dp=[[0 for _ in range(capacity+1)] for _ in range(len(arr)+1)]
    
    
    for i in range(len(dp)):
        for j in range(len(dp[0])):
            
            if i==0:
                dp[i][j]=0
            else:
                if arr[i-1][0]>j:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=max(dp[i-1][j-arr[i-1][0]]+arr[i-1][1],dp[i-1][j])
    for i in range(len(dp)):
        print(dp[i])
    return dp[-1][-1]
arr=[(2,15),(5,14),(1,10),(3,45),(4,30)]
print(knapsack01(arr,7))

            
    