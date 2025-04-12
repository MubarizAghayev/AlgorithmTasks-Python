# def isAnagram(s, t):
    
#     for i in s:
#         if t.find(i) == -1:
#             return False
    
#     return True


# print(isAnagram("anagram","nagaram"))



def isAnagram(s, t):
    
    if len(s) != len(t):
        return False
            
    return sorted(s) == sorted(t)
        


print(isAnagram("anagram","nagaram"))