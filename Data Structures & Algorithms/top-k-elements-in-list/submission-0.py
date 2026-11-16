class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        buckets = [[] for _ in range(len(nums) + 1)]
        res = []

        for n in nums:
            if n in counts:
                counts[n] += 1
            else:
                counts[n] = 1

        for n, v in counts.items():
            buckets[v].append(n)

        for bucket in reversed(buckets):
            for num in bucket:
                res.append(num)

                if len(res) == k:
                    return res
