def containsDuplicate(nums):
    hashmap = {}

    for num in nums:
        if num in hashmap:
            return True
        else:
            hashmap[num] = True
    return False

nums = [1,2,3,1]
print(containsDuplicate(nums))

# time = O(n), space = O(n)

def containsDuplicate2(nums):
    nums.sort()
    for i in range(1,len(nums)):
        if nums[i] == nums[i-1]:
            return True

print(containsDuplicate2(nums))

# time = O(nlog(N)), space = O(1)