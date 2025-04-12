def getConcatenation(nums):
    ans = [0] * (len(nums) * 2)
        
    for i in range(len(nums)):
            
        ans[i] = nums[i]
        ans[i+len(nums)] = nums[i]
                
    return ans

print(getConcatenation([1,2,3,4]))