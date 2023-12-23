class Solution:
    def topKFrequent(nums, k):
        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
            # print(count)
        for n, c in count.items():
            freq[c].append(n)
            # print(freq)
        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                print(res)
                if len(res) == k:
                    return res


nums = [1, 1, 1, 2, 2, 3]
k = 3
Solution.topKFrequent(nums, k)
