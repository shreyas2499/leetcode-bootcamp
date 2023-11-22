class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        flag = [[0]*(n+1)for i in range (m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if text1[i-1] == text2[j-1]:
                    flag[i][j] = flag[i-1][j-1] +1
                else:
                    flag[i][j] = max(flag[i-1][j],flag[i][j-1])
        return flag[m][n] 