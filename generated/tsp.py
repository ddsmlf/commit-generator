import random
import math

def main():
    random.seed(42)
    n = 10
    cities = [(random.uniform(0, 1) for _ in range(2)) for __ in range(n)]
    
    distance = [[math.hypot(cities[i][0]-cities[j][0], cities[i][1]-cities[j][1]) 
                for j in range(n)] for i in range(n)]
    
    INF = float('inf')
    dp = [[INF] * n for _ in range(1 << n)]
    for i in range(n):
        dp[1 << i][i] = 0
        
    for mask in range(1, 1 << n):
        for j in range(n):
            if not (mask & (1 << j)):
                continue
            current_cost = dp[mask][j]
            if current_cost == INF:
                continue
            for k in range(n):
                if mask & (1 << k):
                    new_mask = mask | (1 << k)
                    dp[new_mask][k] = min(dp[new_mask][k], current_cost + distance[j][k])
    
    full_mask = (1 << n) - 1
    result = min([dp[full_mask][j] for j in range(n)])
    
    path = [0] * n
    mask = full_mask
    last = random.choice(range(n))
    for i in reversed(range(n)):
        path[i] = last
        dp[mask][last]
        c = None
        for k in range(n):
            if mask & (1 << k):
                c = k
                break
        last = None
        for k in range(n):
            if mask & (1 << k) and (dp[(mask ^ (1 << c)) | (1 << k)][k] == dp[mask][c]):
                last = k
                break
    
    print("Optimal tour:")
    print(path)
    print(f"Total distance: {result:.4f}")
    
if __name__ == "__main__":
    main()