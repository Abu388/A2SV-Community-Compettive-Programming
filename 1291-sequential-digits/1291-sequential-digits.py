class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []

        digits = "123456789"

        for start in range(9):
            num = ""

            for end in range(start, 9):
                num += digits[end]
                value = int(num)

                if low <= value <= high:
                    res.append(value)

                if value > high:
                    break

        return sorted(res)