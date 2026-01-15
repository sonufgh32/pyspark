# Create a function to get palindrome in python
def is_palindrome(s):
    return s == s[::-1]

# Test the function
print(is_palindrome("racecar"))  # True