"""
集合 s 包含从 1 到 n 的整数。不幸的是，因为数据错误，导致集合里面某一个数字复制成了集合里面的另外一个数字的值，导致集合 丢失了一个数字 并且 有一个数字重复 。

给定一个数组 nums 代表了该集合发生错误后的结果。

请你找出重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。



示例 1：

输入：nums = [1,2,2,4]
输出：[2,3]
示例 2：

输入：nums = [1,1]
输出：[1,2]


提示：

2 <= nums.length <= 10^4
1 <= nums[i] <= 10^4
"""
from operator import index
from typing import List


class Solution:
    """数组法"""
    def findErrorNums(self, nums: List[int]) -> List[int]:
        """
        数组法
        时间复杂度：O(n)
        空间复杂度：O(n)
        :return:
        """
        n = len(nums)
        count = [0] * (n + 1)
        for num in nums:
            count[num] += 1

        duplicate = missing = 0
        for i in range(1, n + 1):
            if count[i] == 2:
                duplicate = i
            elif count[i] == 0:
                missing = i
        return [duplicate, missing]
    """原地哈希交换法"""
    def getConcatenation(self, nums: List[int]) -> List[int]:
        """
        原地哈希交换法
        时间复杂度：O(n)
        空间复杂度：O(1)
        :param nums:
        :return:
        """
        n = len(nums)
        i = 0
        while i < n:
            correct_idx = nums[i] - 1
            if nums[i] != nums[correct_idx]:
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
            else:
                i += 1
        # nums = sorted(nums)

        for i in range(n):
            if nums[i] != i + 1:
                print([nums[i], i + 1])
                return [nums[i], i + 1]

        return []  # 不会执行到这里



if __name__ == '__main__':
    nums = [1,3,1,4,2,5]
    Solution().getConcatenation(nums)
