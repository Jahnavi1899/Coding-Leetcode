def detectCycleBFS(node, adjList, visited):
    queue = [[node, -1]]
    visited[node] = 1

    while queue:
        front, parent = queue.pop(0)
        for adj in adjList[front]:
            if visited[adj] == 0:
                visited[adj] = 1
                queue.append([adj, front])
            elif adj != parent:
                return True
    return False

def detectCycleDFS(node, parent, adjList, visited):
    visited[node] = 1
    for adj in adjList[node]:
        if visited[adj] == 0:
            res = detectCycleDFS(adj, node, adjList, visited)
            if res:
                return True
        elif parent != adj:
            return True
    return False


def isCycle(adjList):
    n = len(adjList)
    visited = [0 for _ in range(n+1)]
    for i in range(1, n+1):
        if visited[i] == 0:
            # for bfs
            #return detectCycleBFS(i, adjList, visited)
            # for dfs
            return detectCycleDFS(i, -1, adjList, visited)
    return False

adjList = [0, [2,3], [5,6], [4,7],[3,8],[2], [2],[3,8],[4,7]]#[0, [2,3],[1,4,5],[1,6],[2],[2],[3]] [0, [2,3],[1,5,6],[1,4,7],[3,8],[2],[2],[3,8],[4,7]]
print(isCycle(adjList))
  