
class Solution():
    def twoSum( nums, target):

        for i in range(0, len(nums) - 1, 1):
            for j in range(i + 1, len(nums), 1):
                if nums[i] + nums[j] == target:
                    print([i,j])



test = [2, 7, 11, 15]
targetnum = 22
Solution.twoSum( test, targetnum)