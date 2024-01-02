class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        tree = {i : [] for i in range(numCourses)}
        for i, j in prerequisites :
            tree[i].append(j)

        visited = set()

        def dfs(i):
            if i in visited :
                return False
            if len(tree[i]) == 0:
                return True

            visited.add(i)
            for neighbor in tree[i]:
                if not dfs(neighbor) :
                    return False
            visited.remove(i)
            tree[i] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True

        
        