# Problem: C - Maedot's Apple Tree - https://codeforces.com/gym/602812/problem/C

testcase = int(input())

for _ in range(testcase):
    n = int(input())
    
    graph = [[] for _ in range(n+1)]
    
    for _ in range(n-1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    ways = [0 for _ in range(n + 1)] #the number of ways each apple will fall
    
    
    
    
    def dfs(root):
        # The stack is holding (node, parent, state)
        # state means are we returning to the node or is it the first time we visit it 
        stack = [(root, 0, 0)]  # since the root node has no parent  
        seen = [0 for _ in range(n + 1)]
        
        # here we mark whatever is in the stack as seen so . . .
        seen[root] = 1 
        
        while stack:
            node, parent, state = stack.pop()
            
            if state == 1:
                # This means we are returning from a call 
                
                is_leaf = True
                
                for nbr in graph[node]:
                    if nbr != parent:
                        is_leaf = False
                        ways[node] += ways[nbr]
                
                if is_leaf:
                    ways[node] = 1 
                        
        
                # WE HAVE TO CONTINUE SINCE WE DO NOT WANT TO RE APPEND 
                continue 
            
            stack.append((node, parent, 1))
            
            for nbr in graph[node]:
                if not seen[nbr]:
                    stack.append((nbr, node, 0)) # append with state 0 since this is the first time we visit it
                    seen[nbr] = 1
            
    
    dfs(1)
    
    
    
    
    q = int(input())

    # now for each pair a b we just return ways of a * ways of b
    for _ in range(q):
        a, b = map(int, input().split())
        
        print(ways[a] * ways[b])
