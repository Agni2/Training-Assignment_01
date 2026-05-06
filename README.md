# Training-Assignment_01

## Problem 1: Cyclic Substring Maximum Sum
You are given a string S consisting of lowercase English alphabets. Each character has a value equal to its position in the alphabet (i.e., a=1, b=2, ..., z=26). 

You are allowed to perform the following operation:
• Choose any cyclic substring of the string (i.e., substring can wrap from end to beginning).

Your task is to:
• Find the maximum possible sum of character values from any cyclic substring such that no character appears more than once in the chosen substring.  

### Input Format: 
• A single line containing the string S.  
### Output Format: 
• Print A single integer representing the maximum sum.  
### Constraints: 
• 1 <= |S| <=10^5. 

## Example:
### Input: 
abca   
### Output: 
6   

## Explanation: 
Possible unique cyclic substrings include 
• "abc" --> sum = 1+2+3=6, 
• "bca" --> sum = 2+3+1=6$, 
• "cab" --> sum = 3+1+2=6. 

Maximum = 6.  
