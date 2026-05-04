# Training-Assignment_01

## Problem 1: Cyclic Substring Maximum Sum
You are given a string $S$ consisting of lowercase English alphabets. Each character has a value equal to its position in the alphabet (i.e., $a=1, b=2, \dots, z=26). Your task is to:
Find the maximum possible sum of character values from any cyclic substring (a substring that can wrap from the end of the string back to the beginning) such that no character appears more than once in the chosen substring.  Input Format: A single line containing the string $S$.  Output Format: A single integer representing the maximum sum.  Constraints: $1 < |S| [cite_start]\le 10^5$.  Example:Input: abca   Output: 6   Explanation: Possible unique cyclic substrings include "abc" ($1+2+3=6$), "bca" ($2+3+1=6$), and "cab" ($3+1+2=6$). The maximum is 6.  
