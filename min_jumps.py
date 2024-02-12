import sys
arr=[3,2,4,2,0,2,3,1,2,2]

def min_jumps(arr): 
    dp=[None]*(len(arr)+1)
    dp[-1]=0
    for n in range(len(arr)-1,-1,-1):
        if arr[n]>0:
            mins=float('inf')
            for i in range(1,arr[n]+1):
                if n+i<=len(arr):
                    if dp[n+i]!=None:
                        
                        mins=min(mins,dp[n+i])
        if mins!=float('inf'):
            dp[n]=mins+1
                                    
            
        
    print(dp)
    return dp[0]
            
print(min_jumps(arr))       
        
        