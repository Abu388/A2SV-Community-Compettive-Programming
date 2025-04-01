# Problem: E - Symmetrization - https://codeforces.com/gym/586960/problem/E

t= int(input())
for _ in range(t):
    n = int(input())
    matrix=[list(map(int,input())) for _ in range(n)]
    res=0
    
    for row in range(n//2):
        for col in range(row,n-1-row):
            dec=[(row,col),(col,n-1-row),(n-1-row,n-1-col),(n-1-col,row)]

            count_zero=0
            count_one=0
            
            for a,b in dec:
                if matrix[a][b]==0:
                    count_zero+=1
                else:
                    count_one+=1
            res+=min(count_one,count_zero)
        
    
    print(res)