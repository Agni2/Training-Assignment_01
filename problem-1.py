import sys

def solve():
    s = sys.stdin.read().strip()
    if not s:
        return
    
    n = len(s)
    max_sum = 0
    limit = min(n, 26)

    for i in range(n):
        seen = set()
        current_sum = 0
        for j in range(limit):
            idx = (i + j) % n
            char = s[idx]
            
            if char in seen:
                break
            
            seen.add(char)
            current_sum += (ord(char) - 96)
            
            if current_sum > max_sum:
                max_sum = current_sum
                
    print(max_sum)

if __name__ == "__main__":
    solve()
