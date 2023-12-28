# Example 1:
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:
#
# Input: nums = [3,3], target = 6
# Output: [0,1]


# решать буду методом двух указателей - он работает
# только на отсортированном массиве


class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        nums_sorted = sorted(nums)
        left = 0
        right = len(nums_sorted) - 1
        # left = nums_sorted[0]
        # right = nums_sorted[len(nums) - 1]
        while left < right:
            sum = nums_sorted[left] + nums_sorted[right]
            if sum == target:
                return left, right
            elif sum > target:
                right -= 1
            else:
                left += 1
        #print(left, right) # этот способ для литкода, там testcase подставляются

# метод two_sum принимает три параметра: self, nums и target.
# для второго и третьего параметра - при вызове метода необходимо передать значения.

# экземпляр класса Solution
solution = Solution()

# вызов метода two_sum у созданного объекта solution и вывод на печать
print(solution.two_sum([2, 7, 11, 15], 9))




