# Given a roman numeral, convert it to an integer.

# Input is guaranteed to be within the range from 1 to 3999.

# ACCEPTED SOLUTION
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return False
        adict = {'V': 5,
                 'X': 10,
                 'I': 1,
                 'II': 2,
                 'III': 3,
                 'IV': 4,
                 'IX': 9,
                 'M': 1000,
                 'D': 500,
                 'C': 100,
                 'L': 50,
                 }
        result = 0
        try:
            for idx in range(len(s)-1):
                temp = s[idx].upper()
                next = s[idx+1].upper()

                if temp in adict:
                    if adict[next] > adict[temp]:
                        result -= adict[temp]
                    else:
                        result += adict[temp]
            result += adict[s[-1].upper()]
        except KeyError:
                return False

        return result
