# Problem: D - Bomb Detection Validation - https://codeforces.com/gym/586960/problem/D

def arr(): 
    return list(map(int, input().split()))

def test(): 
    return int(input())

def solu(matrix,n,m):
    cheak = [(0,1),(1,0),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
    for row in range(n):
        for col in range(m):
            if matrix[row][col] == "*":
                continue
            val = matrix[row][col]
            for l,t in cheak:

                nc = col + l
                nr = row + t
                if 0<=nc<len(matrix[0]) and 0<=nr<len(matrix):
                    if  matrix[nr][nc] == "*":
                        val -= 1
            if val != 0 :                
                return "NO"
    return 'YES'

n, m = arr()
matrix = []
for _ in range(n):
    s = input().strip()
    l = [int(i) if i.isdigit() else i if i == '*' else 0 for i in s]  # Convert digits to int, keep '*' as str
    matrix.append(l)

#iteration on matrix
print(solu(matrix,n,m))
