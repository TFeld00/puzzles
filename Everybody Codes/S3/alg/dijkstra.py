import heapq


def dijkstra(graph, starting_vertex):
    distances = {vertex: (float('infinity'), None) for vertex in graph}
    distances[starting_vertex] = (0, None)

    pq = [(0, starting_vertex, None)]
    while len(pq) > 0:
        current_distance, current_vertex, path = heapq.heappop(pq)

        # Nodes can get added to the priority queue multiple times. We only
        # process a vertex the first time we remove it from the priority queue.
        if current_distance > distances[current_vertex][0]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Only consider this new path if it's better than any path we've
            # already found.
            if distance < distances[neighbor][0]:
                distances[neighbor] = (distance, current_vertex)
                heapq.heappush(pq, (distance, neighbor, current_vertex))

    return distances


"""
example_graph = {
    'U': {'V': 2, 'W': 5, 'X': 1},
    'V': {'U': 2, 'X': 2, 'W': 3},
    'W': {'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5},
    'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
    'Y': {'X': 1, 'W': 1, 'Z': 1},
    'Z': {'W': 5, 'Y': 1},
}
print(dijkstra(example_graph, 'X'))
"""
# => {'U': 1, 'W': 2, 'V': 2, 'Y': 1, 'X': 0, 'Z': 2}


def get_dijkstra_path(distances, target_vertex):
    _, prev = distances[target_vertex]
    path = [prev]
    while distances[prev][1] is not None:
        prev = distances[prev][1]
        path += [prev]
    return path[::-1]
