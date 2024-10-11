class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr, ans = sorted(nums), []           #  <-- 1)
        
        for num in nums:
            i = bisect_left(arr,num)          #  <-- 2a)
            ans.append(i)                     #  <-- 2b)
            del arr[i]                        #  <-- 2c)
            
        return ans                            #  <-- 3)

        