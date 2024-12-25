class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = [0 for i in range(numCourses)]
        pathVisited = visited.copy()
        stack=[]
        adj = {keys :[] for keys in range(numCourses)}
        for i in range(len(prerequisites)):
            adj[prerequisites[i][0]].append(prerequisites[i][1])
        print(adj)
        def dfscheck(i,adj,visited,pathVisited):
            visited[i]=1
            pathVisited[i]=1
            for x in adj[i]:
                if(visited[x]!=1):
                    if(dfscheck(x,adj,visited,pathVisited)==True):
                        return True
                elif(pathVisited[x]==1):
                    return True
            
            stack.append(i)
            pathVisited[i]=0
            return False

        for i in range(len(adj)):
            print(i)
            if(visited[i]!=1):
                if(dfscheck(i,adj,visited,pathVisited)==True):
                    return []
        
        return (stack)