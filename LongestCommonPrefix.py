def longestCommonPrefix(strs):
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]  # shorten prefix one char at a time
            if not prefix:
                return ""
    
    return prefix

        
print(longestCommonPrefix(["flower","flow","flight"]))