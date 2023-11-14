class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        
#       I have the occurences of each number in count
        for i in nums:
            count[i] = count.get(i, 0) + 1
        
#       Need to populate the freq list
#       1 -> Append all elements which are occuring once
        for j, c in count.items():
            freq[c].append(j)
        
        res = []
        for a in range(len(freq)-1, 0, -1):  # Returns -> Most occuring list in the first
            for l in freq[a]:  # Now looping within each list to get the top K values
                res.append(l)
                print(res)
                print(k)
                if(len(res) == k):
                    return res
        
        
    