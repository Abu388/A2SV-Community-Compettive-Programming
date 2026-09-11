from typing import List

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        unique_numbers = set()
        n = len(digits)
        used = [False] * n

        def backtrack(current_digits: List[int]):
            # Base case: we picked 3 digits
            if len(current_digits) == 3:
                # Check constraints:
                # 1. No leading zero (first digit != 0)
                # 2. Must be even (last digit % 2 == 0)
                if current_digits[0] != 0 and current_digits[2] % 2 == 0:
                    number = current_digits[0] * 100 + current_digits[1] * 10 + current_digits[2]
                    unique_numbers.add(number)
                return

            # Try picking any unused digit from anywhere in the array
            for i in range(n):
                if not used[i]:
                    used[i] = True
                    current_digits.append(digits[i])

                    backtrack(current_digits)

                    # Backtrack (undo state)
                    current_digits.pop()
                    used[i] = False

        backtrack([])
        return len(unique_numbers)