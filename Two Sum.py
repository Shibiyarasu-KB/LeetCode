class Solutions:
    def twoSum(self,nums:list[int],target:int)->list[int]:
        d={}
        for i in range(0,len(nums)):
            value=nums[i]
            difference=target-value
            if value not in d:
                d[difference]=i
            else:
                current_index=i
                prev_index=d[value]
                return [current_index,prev_index]