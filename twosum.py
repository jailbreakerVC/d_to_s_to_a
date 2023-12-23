class Solution:
    def twoSum(nums, target):
        for i in range(len(nums)):
            sum = nums[i]
            print("initial sum is", sum, "at index", i)
            for j in range(len(nums)):
                if i != j:
                    sum += nums[j]
                    print("sum is", sum, "at index", j)
                    if sum == target:
                        print("found target at index", i, "and", j)
                        return [i, j]
                    else:
                        sum -= nums[j]
nums = [3, 3]
target = 6
Solution.twoSum(nums, target)
