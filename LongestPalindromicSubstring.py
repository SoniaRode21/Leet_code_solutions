'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"

'''
class Solution:

        
    def isPall(s):
        if s==s[::-1]:
            return len(s)
        else :
            return 0
    def longestPalindrome(self, s: str) -> str:


        """
        :type s: str
        :rtype: str
        """
        count=0
        pallS=""
        if len(s)==1:
            return s
        for index in range(len(s)):
            if index==0:
                i=0
            else :
                i=index-1
            j=index
            
            while i>=0 and j<len(s):
                if s[i]==s[j]:
                    i-=1
                    j+=1
                    if len(pallS)<Solution.isPall(s[i+1:j]):
                        pallS=s[i+1:j]
                else:
    
                                              
                    break
            if index==0:
                i=0
            else :
                i=index-1
            j=index+1
            while i>=0 and j<len(s):
                if s[i]==s[j]:
                    i-=1
                    j+=1
                    if len(pallS)<Solution.isPall(s[i+1:j]):
                        pallS=s[i+1:j]
                else:
                    

                                              
                    break
        return pallS
                
                
            
        

    