class Solution:
    def twoSum(numbers: list[int], target):
        l = 0
        r = len(numbers)-1
        while l < r:
            sum = numbers[l]+numbers[r]
            if sum > target:
                r -= 1
            elif sum < target:
                l += 1
            else:
                return [l+1, r+1]
        return []
#         subarr = []
#         mid_point = round(len(numbers)/2)
#         print("midpoint: index", mid_point, "value", numbers[mid_point])
#         if (target > numbers[len(numbers)-1]) or (target <= 0):
#             print("cas31")
#             subarr = numbers
#         else:
#             print("case2")
#             for i in range(len(numbers[mid_point:len(numbers)])):
#                 print(numbers[i+mid_point])
#                 if target < numbers[i+mid_point]:
#                     subarr = numbers[0:i+mid_point]
#                 elif target > numbers[i+mid_point]:
#                     subarr = numbers[i+mid_point:len(numbers)+1]
#         pri
#         for i in range(len(subarr)):
#             sum = subarr[i]
#             for j in range(len(subarr)):
#                 if i != j:
#                     sum += subarr[j]
#                     print("Sum here: ", sum)
#                     if sum == target:
#                         adder = (len(numbers) - len(subarr))
#                         return [i+adder, j+adder]
#                     else:
#                         sum -= subarr[j]


output = Solution.twoSum([-1000, -1, 0, 1], 1)

print(output)
