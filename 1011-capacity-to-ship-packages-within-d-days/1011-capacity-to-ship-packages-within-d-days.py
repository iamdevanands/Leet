class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        def can_ship(k):
            total_days = 1
            current_load = 0

            for weight in weights:
                if current_load + weight > k:
                    total_days += 1
                    current_load = weight
                else:
                    current_load += weight

            return total_days <= days

        while left <= right:
            mid = left + (right - left) // 2

            if can_ship(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left