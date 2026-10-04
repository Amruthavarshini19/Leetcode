class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        dist = [float('inf')] * n
        dist[src] = 0
        for _ in range(k + 1):
            temp = dist[:]
            for u, v, price in flights:
                if dist[u] != float('inf'):
                    temp[v] = min(temp[v], dist[u] + price)
            dist = temp
        if dist[dst] == float('inf'):
            return -1
        return dist[dst]
        