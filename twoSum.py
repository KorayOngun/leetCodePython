# brute force
nums = [2,7,11,15]
target = 9

for i in range(len(nums)-1):
    for j in range(i+1,len(nums)):
        if nums[i] + nums[j] == target:
            print([i,j])

#Python3
# Runtime 3624 ms Beats 9.28%
# Memory 14.9 MB Beats 100%

#----------------------------------------------

# two pointer
        
sorted_nums = nums.copy()
sorted_nums.sort()
start = 0
end = len(nums)-1
while start < end:
    if sorted_nums[start] + sorted_nums[end] > target:
        end = end-1
    elif sorted_nums[start] + sorted_nums[end] < target:
        start = start + 1
    else:
        x = nums.index(sorted_nums[start])
        y = nums.index(sorted_nums[end], x + 1 if sorted_nums[start] == sorted_nums[end] else 0 )
        return [min(x,y),max(x,y)]

#Python3
# Runtime 59 ms Beats 86.66%
# Memory 17.2 MB Beats 71.33%
