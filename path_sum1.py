#path_sum_dynaminc programming

arr=[5,4,2,7,2,1,3]

def path_sum_dynaminc(arr,target):
    dp=[[0 for i in range(target+1)] for i in range(len(arr)+1)]

    for i in range(len(dp)):
        for j in range(len(dp[0])):
            if i==0 and j==0:
                dp[i][j]=True
            elif i==0:
                dp[i][j]=False
            elif j==0:
                dp[i][j]=True
            else:
                val=arr[i-1]
                if j>=val:
                    if dp[i-1][j]==True:
                        dp[i][j]=True
                    else:
                        dp[i][j]=dp[i-1][j-arr[i-1]]
                
                
                    
    for i in range(len(dp)):
        print(dp[i])
    return dp[-1][-1]
print(path_sum_dynaminc(arr,10))


    
