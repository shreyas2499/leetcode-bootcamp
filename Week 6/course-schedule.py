class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adjlist = {i: [] for i in range(numCourses)}

        for a,b in prerequisites:
            adjlist[b].append(a)
        
        visited = set()
        stack = set()
        # check if it a cyclic directed graph, if Yes, return True
        def dfs(node):
            visited.add(node)
            stack.add(node)
            for n in adjlist[node]:
                if n in stack:
                    return True
                if n not in visited:
                    if dfs(n):
                        return True
            
            stack.remove(node)
            return False

        


        # If it a cyclic grpah, then you can't finish the course, return False
        for i in range(numCourses):
            if i not in visited:
                if dfs(i):
                    return False
        
        return True