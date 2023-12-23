from collections import defaultdict


def Solution(strs):
    res = defaultdict(list)  # mapping char count of each string
    for s in strs:
        count = [0]*26
        for c in s:
            count[ord(c)-ord("a")] += 1

        res[tuple(count)].append(s)
        print(res.keys())
    print(res.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
Solution(strs)
