# In this we calculate the running sum and check if it is in hashmap.If yes then we return the index
# Time Complexity = O(n)
# Space Complexity = O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {}

        for i in range(0,len(nums)):
            hashmap[nums[i]] = i



        for i in range(0,len(nums)):
            comp = target - nums[i]
            if comp in hashmap.keys() and hashmap[comp]!=i:
                return [hashmap[comp],i]
        



