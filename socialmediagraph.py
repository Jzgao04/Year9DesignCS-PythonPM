'''
from collections import deque
graph = {}
queries = []
def accept_values():
    
    vertex_edge = [int(i) for  i in input().strip().split(" ")]
    
    for i in range(vertex_edge[1]):
        edge = [int(i) for i in input().strip().split(" ")]
        try:
            graph[edge[0]].append(edge[1])
        except:
            graph[edge[0]] = [edge[1]]
        try:
            graph[edge[1]].append(edge[0])
        except:
            graph[edge[1]] = [edge[0]]
    
    number_of_queries = int(input())
    for i in range(number_of_queries):
        queries.append([int(i) for i in input().strip().split(" ")])
   
    for query in queries:
        bfs(query)

def bfs(query):
    counter = 0
    q = deque()
    q.append(query[0])
    visited = {query[0] : True}
    distance = {query[0] : 0}
    while q:
        popped = q.popleft()
        for neighbour in graph[popped]:
            if neighbour not in visited:
                visited[neighbour] = True
                
                if distance[popped] + 1 > query[1]:
                    for key in distance:
                        if distance[key] == query[1]:
                          counter +=1
                    print(counter)
                    return
                
                else:
                    distance[neighbour] = distance[popped] + 1
                    q.append(neighbour)
    
    print(counter)

accept_values()

9 10
1 2
2 3
1 7
2 4
3 4
4 7
7 8
9 7
7 6
5 6
3
4 2
5 3
2 1
'''

from collections import defaultdict
 
def bfs(origin, distance, adj, n):
    visited = [False]*(n+1)
    q = []
    dist = [0]*(n+1)
    q.append(origin)
    ans = 0
    while(q):
        u = q.pop(0)
        visited[u] = True
        for i in adj[u]:
            if(visited[i] == False):
                q.append(i)
                visited[i] = True
                dist[i] = dist[u] + 1
                if(dist[i] == distance):
                    ans+=1
                elif(dist[i] > distance):
                    continue
    return ans
    
 
def main():
    adj = defaultdict(list)
    n,e = map(int, input().split(' '))
    for i in range(e):
        u,v = map(int, input().split(' '))
        adj[u].append(v)
        adj[v].append(u)
 
    t = int(input())
    while(t):
        x,y = map(int, input().split(' '))
        print(bfs(x,y,adj,n))
        t-=1
if __name__ == "__main__":
    main()
