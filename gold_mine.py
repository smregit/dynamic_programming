

board=[[0,1,4,2,8,2],
       [4,3,6,5,0,4],
       [1,2,4,1,4,6],
       [2,0,7,3,2,2],
       [3,1,5,9,2,4],
       [2,7,0,8,5,1]]
def goldmine(board):

    dp=[[0 for i in range(len(board[0]))] for _ in range(len(board))]
    row=len(board)
    col=len(board[0])

    for j in range(col-1,-1,-1):


        for i in range(row-1,-1,-1):
            maxs=float("-inf")
            if j+1<col:

                for c in range(1,4):

                        if i-2+c<row and i-2+c>=0:
                            maxs=max(maxs,dp[i-2+c][j+1])
                            dp[i][j]=maxs+board[i][j]
            else:
                dp[i][j]=board[i][j]
    for i in dp:
        print(i)
    res=0
    for i in range(len(board)):
        res=max(res,dp[i][0])
    return res
print(goldmine(board))
