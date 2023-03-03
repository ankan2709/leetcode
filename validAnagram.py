# using stack, time = O(n), space = O(n)









# using the concept of hasing, time = O(n), space = O(n)
def validAnagram(str1, str2):

    dict1 = {}
    dict2 = {}

    for item in str1:
        if item in dict1:
            dict1[item] += 1
        else:
            dict1[item] = 1

    for item in str2:
        if item in dict2:
            dict2[item] += 1
        else:
            dict2[item] = 1

    return dict1 == dict2

s = "anagram"
t = "nagaram"
print(validAnagram(s,t))

s = "rat"
t = "car"
print(validAnagram(s,t))