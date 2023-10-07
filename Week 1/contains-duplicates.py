class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        val = (len(nums)==len(list(set(nums))))
        return (not val)