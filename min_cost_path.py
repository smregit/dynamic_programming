
board=[[2,8,4,1,6,4,2],
       [6,0,9,5,3,8,5],
       [1,4,3,4,0,6,5],
       [6,4,7,2,4,6,1],
       [1,0,3,7,1,2,7],
       [1,5,3,2,3,0,9],
       [2,2,5,1,9,8,2]]
def min_cost_path(board):
    dp=[[0 for _ in range(len(board[0]))] for i in range(len(board))] 
    print(dp)
    row=len(board)-1
    col=len(board[0])-1
    
    
    for i in range(row,-1,-1):
        
        for j in range(col,-1,-1):
            if i+1<=row and j+1>col:
                dp[i][j]=dp[i+1][j]+board[i][j]
            elif j+1<=col and i+1>row:
                dp[i][j]=dp[i][j+1]+board[i][j]
            elif i+1<=row and j+1<=col:
                dp[i][j]=min(dp[i+1][j],dp[i][j+1])+board[i][j]
            else:
                dp[i][j]=board[i][j]
    print(dp)
    return dp[0][0]
print(min_cost_path(board))


                
            
                