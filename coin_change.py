

def coin_change(coins,target):
    #permuation where subsets are used
    dp=[0]*(target+1)
    dp[0]=1
    for i in range(len(coins)):
        for j in range(arr[i],len(dp)):
            dp[j]+=dp[j-arr[i]]
    print(dp)
    return dp[target]
def coin_ch(coins,target):
    #combination where subsequence is used
    dp=[target+1]*(target+1)
    dp[0]=0
    for i in range(len(dp)):
        for c in coins:
            if i-c>=0:
                dp[i]=min(dp[i],1+dp[i-c])
    if dp[target]!=target+1:
        return dp[target]
    else:
        return -1            
    
arr=[2,3,5,6,10]
print(coin_change(arr,10))
print(coin_ch(arr,10))

    
        
    