"""
给定一个二进制数组 nums ， 计算其中最大连续 1 的个数。



示例 1：

输入：nums = [1,1,0,1,1,1]
输出：3
解释：开头的两位和最后的三位都是连续 1 ，所以最大连续 1 的个数是 3.
示例 2:

输入：nums = [1,0,1,1,0,1]
输出：2

提示：

1 <= nums.length <= 105
nums[i] 不是 0 就是 1.
"""
from typing import List


class Solution:
    def findMaxConsecutiveOnes_v1(self, nums: List[int]) -> int:
        """7ms"""
        result = 0
        tmp = 0
        for i in nums:
            if i == 1:
                tmp += 1
            else:
                if tmp > result:
                    result = tmp
                tmp = 0
        print(result)
        return result
    def findMaxConsecutiveOnes_v2(self, nums: List[int]) -> int:
        """23ms"""
        a = str(nums).replace("[","").replace("]","").replace(", ", "").split("0")
        print(a)
        print(max((len(s) for s in a), default=0))
        print(len(max(a, key=len, default=None)))
        print(max(a, key=len, default=None))
        return max((len(s) for s in a), default=0)


if __name__ == '__main__':
    nums = [1,0,1,1,0,1]
    solution = Solution().findMaxConsecutiveOnes_v2(nums)