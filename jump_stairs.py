#arr=[3,3,0,2,2,3]
#dp =[8,5,0,3,2,1,1]

def jump_stairs(arr):
    dp=[0]*(len(arr)+1)
    dp[-1]=1
    
    for i in range(len(dp)-2,-1,-1):
        
        for j in range(1,arr[i]+1):
            if j+i<len(dp):
                dp[i]+=dp[i+j]
    print(dp)
    return dp[0]
arr=[3,3,0,2,2,3]
print(jump_stairs(arr))
    
    
        
    
    
    