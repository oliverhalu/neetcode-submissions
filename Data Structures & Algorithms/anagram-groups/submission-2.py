class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # (a:1,b:1,c:1) : [abc,cba,bca]
        frequencies = {}
        for s in strs:
            freq = {}
            for c in s:
                freq[c] = freq.get(c, 0) + 1
            frequencies.setdefault(tuple(sorted(freq.items())), []).append(s)

        return list(frequencies.values())