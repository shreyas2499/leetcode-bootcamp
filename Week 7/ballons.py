class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        cnt=0;maxr=points[0][1]
        for i in range(1,len(points)):
            if maxr>=points[i][0]:
                maxr=min(maxr,points[i][1])
            else:
                cnt+=1
                maxr=points[i][1]
        return (cnt+1)
        