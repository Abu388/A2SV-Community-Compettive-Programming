class Solution:
    def strongPasswordChecker(self, s: str) -> int:
        missing = 3
        missing -= any(c.islower() for c in s)
        missing -= any(c.isupper() for c in s)
        missing -= any(c.isdigit() for c in s)

        n = len(s)
        replace = one = two = 0

        i = 2
        while i < n:
            if s[i] == s[i - 1] == s[i - 2]:
                l = 2
                while i < n and s[i] == s[i - 1]:
                    l += 1
                    i += 1

                replace += l // 3

                if l % 3 == 0:
                    one += 1
                elif l % 3 == 1:
                    two += 1
            else:
                i += 1

        if n < 6:
            return max(missing, 6 - n)

        if n <= 20:
            return max(missing, replace)

        delete = n - 20

        use = min(delete, one)
        replace -= use
        delete -= use

        use = min(delete // 2, two)
        replace -= use
        delete -= use * 2

        replace -= min(replace, delete // 3)

        return (n - 20) + max(missing, replace)