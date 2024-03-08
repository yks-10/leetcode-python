class Solution:
    def test(self, colors: list, c: int) -> bool:
        alice = "A"
        bob = "B"
        count = c
        result = None
        for i in range(len(colors) - 1):
            if count % 2 == 0:
                rem = alice
            else:
                rem = bob
            if colors.count(rem) >= 2:
                if colors[i] == colors[i + 1] == rem:
                    if i == 0:
                        colors.pop(i + 1)
                    else:
                        colors.pop(i)
                    count += 1
                    break
                if i == len(colors) - 2:
                    if rem != alice:
                        result = True
                    else:
                        result = False

        if result is None:
            return self.test(list(colors), count)
        else:
            return result

    def winnerOfGame(self, colors: str) -> bool:
        colors = list(colors)
        return self.test(colors, 0)


x = Solution()
print(x.winnerOfGame("AAABABB"))  # Output: False
