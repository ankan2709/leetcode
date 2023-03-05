# efficient using two pointers: Linear time and constant space

def isPalidrome2(s):
    left = 0
    right = len(s) - 1

    while left < right:
        while left < right and not alphanum(s[left]):
            left += 1
        while right > left and not alphanum(s[right]):
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True


def alphanum(c):
    return (ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9'))

s = "A man, a plan, a canal: Panama"
print(isPalidrome2(s))




# inefficient soln linear time but not constant space infact o(n) space length of the string
def isPalindrone(string):
    newStr = ""

    for char in string:
        if char.isalnum():
            newStr += char.lower()

    return newStr == newStr[::-1]


s = "A man, a plan, a canal: Panama"
print(isPalindrone(s))
