class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        center1 = 0
        center2 = 0
        center = 0
        for index, edge in enumerate(edges):
            if(index == 0): 
                center1 = edge[0]
                center2 = edge[1]
                continue
            if(center1 in edge):
                center = center1
            elif(center2 in edge):
                center = center2
        
        return center
            
            