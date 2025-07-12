def lengthOfLongestSubstring():
    s = "pwwkew"
    n = len(s)

    ans = 0
    left = 0
    right = 0

    s_new = []
    for i in range(n):
        for j in range(i, n):
            if s[i] == s[j]:
                left = s.index(s[i]) - 1 
        
        right += 1

        ans = max(ans, right - left)
        



    return ans



    # ans = 0

    # s_new = []
    # for i in s:
    #     if i in s_new:
    #         ans = max(ans, len(s_new))
    #         s_new.clear()
    #         s_new.append(i)
    #     else:
    #         s_new.append(i)
        
    #     ans = max(ans, len(s_new))

    # return ans

print(lengthOfLongestSubstring())