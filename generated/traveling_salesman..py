import math

# Read input
n = int(input())
cities = []
for _ in range(n):
    x, y = map(int, input().split())
    cities.append((x, y))

# Function to calculate distance between two points
def distance(p1, p2):
    return math.hypot(p1[0]-p2[0], p1[1]-p2[1])

# Precompute all pairwise distances
distances = [[distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Nearest neighbor algorithm to find approximate TSP path
path = [0]
current = 0
visited = [False]*n
visited[current] = True

for _ in range(n-1):
    min_dist = float('inf')
    next_city = -1
    for j in range(n):
        if not visited[j]:
            dist = distances[current][j]
            if dist < min_dist:
                min_dist = dist
                next_city = j
    path.append(next_city)
    current = next_city
    visited[next_city] = True

# Calculate total distance of the path
total_distance = 0.0
for i in range(len(path)-1):
    total_distance += distances[path[i]][path[i+1]]

print(f"Number of cities: {n}")
print("Path:", path)
print(f"Total distance traveled: {total_distance:.2f}")