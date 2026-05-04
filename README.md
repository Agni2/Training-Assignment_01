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

## Problem 2: Array Transformation Cost Minimization
You are given an integer array A of size N. You can perform the following operation any number of times: 
• Choose any index $i$ and replace A[i] with A[i] + K or A[i] - K, where $K$ is a fixed integer.  

Your goal is to:
• Transform the array such that all elements become equal. 
• Return the minimum total number of operations required, or -1 if it is not possible.

### Input Format: 
• First line: Integer N.  
• Second line: N space-separated integers (array A).  
• Third line: Integer K.  

### Output Format: 
• Print the minimum number of operations or -1.  

### Constraints: 
• 1 <=N<=10^5; 
• 1 <=A[i], K <=10^9. 

### Example:
#### Input:
5
2 4 6 8 10
2
#### Output:
6

### Explanation:
Convert all elements to 6:

• 2 -->6(2 steps)
• 4 -->6(1 step)
• 6 -->6(0 step)
• 8 -->6(1 step)
• 10 -->6(2 steps)

Total operations = 6
