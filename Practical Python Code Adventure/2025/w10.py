DAY,_,_=__file__.rpartition('.')


## From W3C
class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size

    def add_edge(self, u, v, c):
        self.adj_matrix[u][v] = c

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def dfs(self, s, t, visited=None, path=None):
        if visited is None:
            visited = [False] * self.size
        if path is None:
            path = []

        visited[s] = True
        path.append(s)

        if s == t:
            return path

        for ind, val in enumerate(self.adj_matrix[s]):
            if not visited[ind] and val > 0:
                result_path = self.dfs(ind, t, visited, path.copy())
                if result_path:
                    return result_path

        return None

    def fordFulkerson(self, source, sink):
        max_flow = 0

        path = self.dfs(source, sink)
        while path:
            path_flow = float("Inf")
            for i in range(len(path) - 1):
                u, v = path[i], path[i + 1]
                path_flow = min(path_flow, self.adj_matrix[u][v])

            for i in range(len(path) - 1):
                u, v = path[i], path[i + 1]
                self.adj_matrix[u][v] -= path_flow
                self.adj_matrix[v][u] += path_flow

            max_flow += path_flow

            path = self.dfs(source, sink)

        return max_flow


r=[]
nodes=set()
with open(f'{DAY}.1.txt','r', encoding='utf8')as F:
    for l in F:
        l=l.rstrip('\n')
        n,v=l.split()
        a,b=n.split('-')
        r+=(a,b,int(v)),
        nodes|={a,b}

nodes = list(nodes)
g = Graph(len(nodes))
for a,b,v in r:
    g.add_edge(nodes.index(a),nodes.index(b),v)

s,t = nodes.index('S1'),nodes.index('MD')
print(g.fordFulkerson(s,t))

# ---

r=[]
nodes=set()
with open(f'{DAY}.2.txt','r', encoding='utf8')as F:
    for l in F:
        l=l.rstrip('\n')
        n,v=l.split()
        if v=='Inf': v=9**9
        a,b=n.split('-')
        r+=(a,b,int(v)),
        nodes|={a,b}

nodes = list(nodes) + ['XXX']
g = Graph(len(nodes))
for a,b,v in r:
    g.add_edge(nodes.index(a),nodes.index(b),v)

for a in '76 77 78 79 80'.split(): #targets
    g.add_edge(nodes.index(a),nodes.index('XXX'),9**9)

s,t = nodes.index('0'),nodes.index('XXX')
print(g.fordFulkerson(s,t))