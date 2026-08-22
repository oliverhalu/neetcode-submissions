class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = nums.count(0)
        # if more then 2 zeros we can return array of 0 of length num
        # because one factor will always be 0
        if zeros >= 2:
            return [0] * len(nums)

    # multiply each non-zero element
        product = 1
        for e in nums: 
            if e != 0:
                product *= e
        
        print("product ", product)
        output = []

        # handle case where nums contains zeros
        if 0 in nums:
            for e in nums:
                if e != 0:
                    output.append(0)
                else:   
                    output.append(product)
        else: 
            for e in nums:
                output.append(int(product / e))

        return output