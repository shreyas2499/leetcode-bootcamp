class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Optimised solution
        charSet = set()
        l = 0
        res = 0
        
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l = l + 1
            charSet.add(s[r])
            res = max(res, r-l+1)
                    
        return res
        

        
        
        #         First Solution
        # l, r = 0, 0
        # arr = ""
        # maxS = 0
        # while r<len(s):
        #     if(s[r] not in arr):
        #         arr = arr + s[r]
        #         maxS = max(maxS, len(arr))
        #         r = r + 1
        #     else:
        #         arr = ""
        #         l = l + 1
        #         r = l
        # # print(arr)
        # # print(maxS)
        # return maxS
        