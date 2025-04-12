def majorityElement(nums):
    
    for i in nums:
        count = 0
        for j in nums:
            if i == j:
                count+=1
            
        if count > len(nums)/2:
            return i
        
print(majorityElement([2,2,1,1,1,2,2]))


# def majorityElement(nums):
    
#     i = 0
#     nums.sort()
#     for j in range(len(nums)):
#         UserList = [0]
#         if nums[i] == nums[j] and nums[i] not in UserList:
#             count+=1
            
#         if count > len(nums)/2:
#             return nums[i]
#         else:
#             UserList.append(nums[i])
#             i+=1
            
# print(majorityElement([2,2,1,1,1,2,2]))