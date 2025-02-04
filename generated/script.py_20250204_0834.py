import itertools

def calc_distance(p1,p2):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5

cities = []
n = int(input())
for _ in range(n):
    x,y = map(int, input().split())
    cities.append((x,y))

from itertools import permutations
all_perm = list(permutations(cities))
min_dist = float('inf')
optimal_path = None

for perm in all_perm:
    total = 0.0
    for i in range(len(perm)):
        p = i
        if i > 0:
            prev_p = perm[i-1]
            total += calc_distance(perm[p],prev_p)
    if total < min_dist:
        min_dist = total
        optimal_path = perm

print("Optimal path:",optimal_path)
print("Total distance:",round(min_dist,2))