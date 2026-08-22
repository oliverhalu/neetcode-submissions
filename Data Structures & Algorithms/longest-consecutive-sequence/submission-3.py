class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0

        num_set = set(nums)
        longest_sequence_length = 1

        for e in num_set:
            if e-1 not in num_set:
                length = 1
                seq_start = e
                while seq_start + 1 in num_set:
                    length += 1
                    seq_start += 1
                if length > longest_sequence_length:
                    longest_sequence_length = length

        return longest_sequence_length