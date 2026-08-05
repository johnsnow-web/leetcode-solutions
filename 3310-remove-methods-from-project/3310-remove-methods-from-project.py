
class Solution:
    def remainingMethods(self, n: int, k: int, invocations: list[list[int]]) -> list[int]:
        # Build adjacency list
        graph = [[] for _ in range(n)]
        
        for a, b in invocations:
            graph[a].append(b)
        
        # Find all suspicious methods (reachable from k)
        suspicious = set()
        def dfs(node):
            suspicious.add(node)
            for neighbor in graph[node]:
                if neighbor not in suspicious:
                    dfs(neighbor)
        
        dfs(k)
        
        # Check if any non-suspicious method invokes a suspicious method
        for a, b in invocations:
            if a not in suspicious and b in suspicious:
                # A non-suspicious method invokes a suspicious method
                return list(range(n))
        
        # Safe to remove all suspicious methods
        return [method for method in range(n) if method not in suspicious]