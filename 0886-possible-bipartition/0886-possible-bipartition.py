class Solution(object):
    def possibleBipartition(self, n, dislikes):
        g = [[] for _ in range(n+1)]
        for a, b in dislikes:
            g[a].append(b)
            g[b].append(a)
        color = [-1] * (n+1)
        for i in range(1,n+1):
            if color[i]!=-1:
                continue
            q = deque([i])
            color[i]=0
            while q:
                u = q.popleft()
                for v in g[u]:
                    if color[v]==-1:
                        color[v] = 1 - color[u]
                        q.append(v)
                    elif color[v] == color[u]:
                        return False
        return True

        