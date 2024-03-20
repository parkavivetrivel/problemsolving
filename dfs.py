graph = {
    'a': ['b', 'c','d'],
    'b': ['e'],
    'c': ['d', 'e'],
    'd': [],
    'e': []
}
# in dfs if we repeat a same connection like A to B and B to A in a graph( we will be facing a recursive error)
# also when visited[] is placed inside the function its printing another 2 elemnets of the graph additionally
visited = []
def main(graph, start, visited):
    if start not in visited:
        print(start)
        visited.append(start)
        for i in graph[start]:
            main(graph,i, visited)

main(graph,'a', visited)