class Solution:
    def isPalindrome(s):
        A = []
        for character in s:
            if (ord('a') <= ord(character) <= ord('z')) or (ord('A') <= ord(character) <= ord('Z')) or (ord('0') <= ord(character) <= ord('9')):
                A.append(character.lower())
                print
        print(A == A[::-1])


s = "0P"
Solution.isPalindrome(s)
