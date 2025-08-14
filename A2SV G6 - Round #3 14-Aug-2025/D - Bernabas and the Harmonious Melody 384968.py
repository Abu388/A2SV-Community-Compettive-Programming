# Problem: D - Bernabas and the Harmonious Melody - https://codeforces.com/gym/588468/problem/D


def arr(): return list(map(int, (x for x in input().split())))#strip
def test(): return int(input())


t  = test()
for _ in range(t):
    n = test()
    s = input()
    value = float('inf')
    set_value = set(s)
    for ch in set_value:# for each set value(for every number)
        left_side , right_side,  = 0 , n - 1
        removal = 0
        while left_side < right_side:
            if s[left_side] == s[right_side]:
                right_side -= 1
                left_side += 1
            else:
                if s[left_side] == ch:
                    removal += 1
                    left_side += 1
                elif s[right_side] == ch:
                    removal += 1
                    right_side -= 1
                else:
                    break
        else:
            value = min(value,removal)
    if value == float('inf'):
        print(-1)
    else:
        print(value)




