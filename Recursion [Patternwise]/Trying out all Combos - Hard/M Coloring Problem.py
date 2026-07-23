# M - Coloring Problem

# Problem Statement: Given an undirected graph and a number m, determine if the graph can be colored with at most m colors such that no two adjacent vertices of the graph are colored with the same color.

def graphColouring(graph, m, n):

    colors = [0] * n

    def isSafe(vertex, color):

        for i in range(n):

            if graph[vertex][i] == 1 and colors[i] == color:
                return False

            return True

    def solve(vertex):

        if vertex == n:
            return True

        for color in range(1, m+1):

            if isSafe(vertex, color):

                colors[vertex] = color

                if solve(vertex + 1):
                    return True

                colors[vertex] = 0

        return False

    return solve(0)

graph = [
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 0],
    [0, 1, 0, 0]
]

n = 4
m = 3

print(graphColouring(graph, m, n))