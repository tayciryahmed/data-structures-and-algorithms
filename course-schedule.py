class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = collections.defaultdict(list)
        indegree = [0] * numCourses
        
        for pr in prerequisites:
            adj[pr[1]] += [pr[0]]
            indegree[pr[0]] += 1

        
        queue = collections.deque()
        count = 0 
        
        for i in range(len(indegree)):
            if indegree[i] == 0:    
                queue.append(i)
            
        while queue:
            curr = queue.popleft()
            if indegree[curr] == 0: count += 1
            if curr not in adj: continue
            
            for neibr  in adj[curr]:
                indegree[neibr] -= 1
                if indegree[neibr] == 0 :
                    queue.append(neibr)
            
        return count == numCourses
            
