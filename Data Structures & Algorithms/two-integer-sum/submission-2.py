class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """for index1 in range (len(nums)):
            for index2 in range (index1+1, len(nums)):
                if nums[index1]+nums[index2] == target:
                    return [index1,index2]
        """

        hashmap = {}
        index=0
        for i in nums:
            hashmap[i]=index
            index+=1

        for index1 in range(len(nums)):
            if target - nums[index1] in hashmap and hashmap[target - nums[index1]]!=index1:
                return [index1,hashmap[target-nums[index1]]]
        

        """
        hashmap key,value  key hashlenen sey
        somethıng ın hm - Burada arama yapar ve sen onun karsılıgını alırsın 
        sayı.ındexı key value
        sayı ındex
        """