def twoSum2(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] + arr[right] == target:
            return [left + 1, right + 1]
        elif arr[left] + arr[right] < target:
            left += 1
        elif arr[left] + arr[right] > target:
            right -= 1

numbers = [2,7,11,15]
target = 9

print(twoSum2(numbers, target))