import collections
graph = {
    'a': ['b', 'e'],
    'b': 'd',
    'c': ['b', 'd'],
    'd': ['e', 'b'],
    'e': ['a', 'c']
}

def bfs(graph, start):
    visited = []
    queue = collections.deque([start])
    while len(queue)!= 0:
        a = queue.popleft()
        if a not in visited:
            visited.append(a)
            for i in graph[a]:
                if i not in visited:
                    queue.append(i)
    return visited
print(bfs(graph,'a'))