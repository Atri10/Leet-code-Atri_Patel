class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        def DFS(path):
            if path[-1] == len(graph) - 1 : ans.append(path)
            else:
                for i in graph[path[-1]]:DFS(path+[i])
                    
        DFS([0])
        return ans