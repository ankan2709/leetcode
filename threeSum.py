
def threeSum(arr):
    arr.sort()
    res = []

    for i, a in enumerate(arr):
        if i > 0 and a == arr[i-1]:
            continue
        left = i + 1
        right = len(arr) - 1

        while left < right:
            three_sum = a + arr[left] + arr[right]

            if three_sum > 0:
                right -= 1
            elif three_sum < 0:
                left += 1
            else:
                res.append([a, arr[left], arr[right]])
                left += 1
                while nums[left] == nums[left-1]:
                    left += 1
    return res


nums = [-1,0,1,2,-1,-4]
res = threeSum(nums)
print(res)