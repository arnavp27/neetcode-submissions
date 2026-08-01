import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in nums:
            product = nums.copy()
            product.remove(i)
            output.append(math.prod(product))
        return output
