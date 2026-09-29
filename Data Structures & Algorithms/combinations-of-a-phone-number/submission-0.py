class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []

        def backtrack(index, word):
            # finished all digits
            if index == len(digits):
                result.append(word)
                return
            
            # try every letter for current digit
            for letter in phone[digits[index]]:
                backtrack(index + 1, word + letter)

        backtrack(0, "")
        return result
