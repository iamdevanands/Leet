class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) <= 2:
            return max(nums)

        def rob_linear(houses):
            curr = 0
            prev = 0

            for i in range(len(houses)):
                temp = curr
                curr = max(curr, prev + houses[i])
                prev = temp

            return curr

        skip_last = rob_linear(nums[:-1])
        skip_first = rob_linear(nums[1:])

        return max(skip_last, skip_first)