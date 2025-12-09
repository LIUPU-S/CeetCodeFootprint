"""
给你一个长度为 n 的整数数组 nums 。请你构建一个长度为 2n 的答案数组 ans ，数组下标 从 0 开始计数 ，对于所有 0 <= i < n 的 i ，满足下述所有要求：

ans[i] == nums[i]
ans[i + n] == nums[i]
具体而言，ans 由两个 nums 数组 串联 形成。

返回数组 ans 。


示例 1：

输入：nums = [1,2,1]
输出：[1,2,1,1,2,1]
解释：数组 ans 按下述方式形成：
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]
示例 2：

输入：nums = [1,3,2,1]
输出：[1,3,2,1,1,3,2,1]
解释：数组 ans 按下述方式形成：
- ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
- ans = [1,3,2,1,1,3,2,1]

提示：

n == nums.length
1 <= n <= 1000
1 <= nums[i] <= 1000
"""
from typing import List

from pycparser.ply.yacc import resultlimit


class Solution:
    def getConcatenation_v1(self, nums: List[int]) -> List[int]:
        """用时7ms"""
        # 最大值限制
        max_numb = len(nums)
        # 最大长长度限制
        max_len = 2 * len(nums)
        # 结果
        result = []

        tmp_i = 0
        while len(result) < max_len:
            if tmp_i >= max_numb:
                tmp_i = 0
            if 0 <= tmp_i < max_numb:
                result.append(nums[tmp_i])
            tmp_i += 1
        return result

    def getConcatenation_v1(self, nums: List[int]) -> List[int]:
        """用时0ms"""
        return nums * 2

if __name__ == '__main__':
    tmp_numbs = [5,8,1,9,9,18,16,1,11,6,8,10]
    Solution().getConcatenation(tmp_numbs)
