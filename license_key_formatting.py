# License Key Formatting

# Now you are given a string S, which represents a software license key which we would like to format.
# The string S is composed of alphanumerical characters and dashes. The dashes split the alphanumerical
# characters within the string into groups. (i.e. if there are M dashes, the string is split into M+1 groups).
# The dashes in the given string are possibly misplaced.

# We want each group of characters to be of length K (except for possibly the first group, which could be shorter,
# but still must contain at least one character). To satisfy this requirement, we will reinsert dashes. Additionally,
# all the lower case letters in the string must be converted to upper case.

# So, you are given a non-empty string S, representing a license key to format, and an integer K. And you need to
# return the license key formatted according to the description above.

# Example 1:
# Input: S = "2-4A0r7-4k", K = 4
# Output: "24A0-R74K"

# Explanation: The string S has been split into two parts, each part has 4 characters.
# Example 2:
# Input: S = "2-4A0r7-4k", K = 3
# Output: "24-A0R-74K"

# Explanation: The string S has been split into three parts, each part has 3 characters except the first part as it
# could be shorter as said above.
# Note:
# The length of string S will not exceed 12,000, and K is a positive integer.
# String S consists only of alphanumerical characters (a-z and/or A-Z and/or 0-9) and dashes(-).
# String S is non-empty.

#Accepted Solution (clumsy)-
class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        if len(S) == 1 and S.isalnum():
            return S.upper()
        if len(S) == 1 and not S.isalnum():
            return ""
        result = ""
        temp = ''.join(S.split('-'))
        char_count = len(temp)
        key_hold = []
        remainder = char_count % K
        new_key = None
        if remainder == 0:
            while K <= char_count:
                new_key = temp[:K]
                key_hold.append(new_key)
                result = '-'.join(key_hold)
                temp = temp[K:]
                char_count = len(temp)
            return result.upper()
        elif remainder != 0:
            key_hold.append(temp[:remainder])
            temp = temp[remainder:]
            while K <= char_count:
                new_key = temp[:K]
                key_hold.append(new_key)
                result = '-'.join(key_hold)
                temp = temp[K:]
                char_count = len(temp)
            return (temp + result).upper()


#Shorter Solution from other submission - MUCH FASTER ALGORITHM WITH .UPPER() AND .REPLACE() (both written in native C)
class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.upper().replace('-','')
        size = len(S)
        s1 = K if size%K==0 else size%K  #Conditional variable assignment!!
        res = S[:s1]
        while s1<size:
            res += '-'+S[s1:s1+K]
            s1 += K
        return res
