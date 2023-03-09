
def threeSum(arr):
    arr.sort()
    res = []

    for i, a in enumerate(arr):
        if i > 0 and a == arr[i-1]:
            continue
        left = i + 1
        right = len(arr) - 1

        while left < right:
            if a + arr[left] + arr[right] == 0:
                res.append([a, arr[left], arr[right]])
                left += 1
                right -= 1
            elif a + arr[left] + arr[right] > 0:
                right -= 1
            elif a + arr[left] + arr[right] < 0:
                left += 1
    return res


nums = [-1,0,1,2,-1,-4]
res = threeSum(nums)
print(res)