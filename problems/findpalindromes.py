def check_palindrome(s):
    if s == s[::-1]:
        return "Strong Palindrome"
    elif s.lower() == s.lower()[::-1]:
        return "Weak Palindrome"
    else:
        return "Not a Palindrome"

n = int(input().strip())
for _ in range(n):
    s = input().strip()
    print(check_palindrome(s))
