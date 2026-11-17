
class Solution:
    def isPalindrome(self, s: str) -> bool:

        revstr = ''

        for i in s:
            if not i.isalnum():
                continue

            revstr = revstr + i.lower()

        return revstr == revstr[::-1]


