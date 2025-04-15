
from collections import defaultdict
def sortArray(nums):
    def counting_sort():
        count = defaultdict(int)
        minVal, maxVal = min(nums), max(nums)
        for val in nums:
            count[val] += 1

        index = 0
        for val in range(minVal, maxVal + 1):
            while count[val] > 0:
                nums[index] = val
                index += 1
                count[val] -= 1

    counting_sort()
    return nums
print(sortArray([5,1,1,2,0,0]))