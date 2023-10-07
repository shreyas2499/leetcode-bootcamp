class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        area = (r - l) * min(height[l], height[r])
        while l<r:
            area = max(area, (r - l) * min(height[l], height[r]))
            if(height[l]<height[r]):
                l = l + 1
            elif(height[l]>height[r]):
                r = r - 1
            elif(height[l]==height[r]):
                l = l + 1
        return area