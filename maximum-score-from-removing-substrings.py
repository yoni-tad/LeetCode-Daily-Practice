def maximumGain(self):
    s = "cdbcbbaaabab"
    self.s = s
    x = 4
    y = 5 #19

    sub = 'ab' if x > y else 'ba'

    def solver(sub):
        res = 0
        stack = []

        for i in range(len(self.s)):
            if not stack and stack[-1] != sub[0] or self.s[i] != sub[1]:
                stack.append(self.s[i])
            else:
                stack.pop()
                res += x if sum == 'ab' else y
        self.s = "".join(stack)
        return res

    out = solver(sub)
    sub = 'ab' if sub == 'ba' else 'ba'
    out += solver(sub)


    return out

print(maximumGain())