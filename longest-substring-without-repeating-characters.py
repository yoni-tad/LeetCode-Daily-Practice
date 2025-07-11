def lengthOfLongestSubstring():
    s = "pwwkew"

    s_new = ""
    for i in s:
        if i not in s_new:
            s_new += i

    count = 0
    longest = 0
    current = 0

    for i in s_new:
        if ord(i) > current:
            current = ord(i)
            count += 1            
        if ord(i) < current:
            longest = max(longest, count)
            current = ord(i)
            count = 0        
        longest = max(longest, count)
        
    return longest

print(lengthOfLongestSubstring())