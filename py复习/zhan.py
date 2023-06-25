from typing import List


class Solution:
    def __init__(self):
        self.nums = []
        self.ans = []
        self.n=0

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.n = len(nums)
        self.backtrack(0)

    def backtrack(self,now_idx):
            if now_idx == self.n - 1:
                self.ans.append(self.nums[:])

            tmp_set = set()
            for i in range(now_idx, self.n):
    # 剪枝条件
                if self.nums[i] in tmp_set:
                    continue
                tmp_set.add(slice.nums[i])
                self.nums[i], self.nums[now_idx] = self.nums[now_idx], self.nums[i]
                self.backtrack(self,now_idx + 1)
                self.nums[i], self.nums[now_idx] = self.nums[now_idx], self.nums[i]
                self.backtrack(0)
            return self.ans

s1 = Solution()
str = input('请输入要排列的数字（用空格隔开）：')
num = [int(i) for i in str.split()]
print(s1.permuteUnique(num))
