def dfs(adj, node, parent, color):
    count_color[color] += 1
    for i in range(len(adj[node])):
        if (adj[node][i] != parent):
            dfs(adj, adj[node][i],node, not color)
            
def findMaxEdges(adj, n):
    dfs(adj, 1, 0, 0)
    return (count_color[0] *count_color[1] – (n – 1))

count_color = [0, 0]
n = int(input())
adj = []
for _ in range(n):
    k = list(map(int,input().split()))
    adj.append(k)
print(findMaxEdges(adj, n))
