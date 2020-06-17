class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        
        for index, numero in enumerate(nums):
            complementar = target - numero
            if complementar not in dic:
                dic[numero] = index
            else:
                return [dic[complementar], index]