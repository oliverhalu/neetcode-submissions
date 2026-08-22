class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # build frequency dict
        # nums = [1,2,2,3,3,3,]
        # freq = {1:1, 2:2, 3:4}
        freq = {}
        for n in nums: 
            freq[n] = freq.get(n, 0) + 1
        # now we need to get a list of keys sorted by values
        sorted_freq = sorted(freq.items(), key=lambda item: item[1])
    
        return [n for n, count in sorted_freq[-k:]]

        