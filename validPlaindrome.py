def isPalindrone(string):
    newStr = ""

    for char in string:
        if char.isalnum():
            newStr += char.lower()

    return newStr == newStr[::-1]


s = "A man, a plan, a canal: Panama"
print(isPalindrone(s))
