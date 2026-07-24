class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        current_subset=[]
        def backtrack(index):
            if index==len(nums):
                result.append(list(current_subset))
                return
            current_subset.append(nums[index])
            backtrack(index+1)
            current_subset.pop()
            backtrack(index+1)
        backtrack(0)
        return result
        