"""
https://leetcode.com/problems/longest-absolute-file-path/
Suppose we have the file system represented in the following picture:



We will represent the file system as a string where "\n\t" mean a subdirectory of the main directory, "\n\t\t" means a subdirectory of the subdirectory of the main directory and so on. Each folder will be represented as a string of letters and/or digits. Each file will be in the form "s1.s2" where s1 and s2 are strings of letters and/or digits.

For example, the file system above is represented as "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext".

Given a string input representing the file system in the explained format, return the length of the longest absolute path to a file in the abstracted file system. If there is no file in the system, return 0.

 

Example 1:


Input: input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
Output: 20
Explanation: We have only one file and its path is "dir/subdir2/file.ext" of length 20.
The path "dir/subdir1" doesn't contain any files.
Example 2:


Input: input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
Output: 32
Explanation: We have two files:
"dir/subdir1/file1.ext" of length 21
"dir/subdir2/subsubdir2/file2.ext" of length 32.
We return 32 since it is the longest path.
Example 3:

Input: input = "a"
Output: 0
Explanation: We don't have any files.
 

Constraints:

1 <= input.length <= 104
input may contain lower-case or upper-case English letters, a new line character '\n', a tab character '\t', a dot '.', a space ' ' or digits.
"""

# time complexity: O(n), space complexity: O(k) where k is the deepest directory depth

class Solution:
    def lengthLongestPath(self, input: str) -> int:
        if '.' not in input:
            return 0
        
        input.replace('    ', '\t')
        
        index = []
        result = 0
        
        name = ''
        num_t = 0

        for i in range(len(input)):
            if 'a' <= input[i] <= 'z' or 'A' <= input[i] <= 'Z' or input[i] == '.' or '0' <= input[i] <= '9' or input[i] == ' ':
                name += input[i]
                if i == len(input) - 1 or input[i+1] == '\n' or input[i+1] == '\t':
                    dir_prefix = index[num_t-1]+1 if num_t > 0 else 0
                    if '.' in name:
                        result = max(result, dir_prefix + len(name))
                    else:
                        while num_t > len(index)-1:
                            index.append(-1)
                        index[num_t] = dir_prefix + len(name)
                    name = ''
                    num_t = 0
            elif input[i] == '\n':
                num_t = 0
            elif input[i] == '\t':
                num_t += 1

        return result 