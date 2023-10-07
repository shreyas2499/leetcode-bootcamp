class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         Results in timeout error
#         i=0
#         j=k
#         res = []
#         for i in range(0, len(nums)+1-k):
#             res.append(max(nums[i:i+k]))
#             nums = nums[]
#         return res


        res = []
        l = r = 0
        
        q = collections.deque()
    
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            
            if(l > q[0]):
                q.popleft()
                
            if (r+1)>=k:
                res.append(nums[q[0]])
                l = l + 1
            r = r + 1
        
        return res