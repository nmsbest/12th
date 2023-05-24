# py program to search for and replace a substring
# Credits: Dhruv , XII-D

def replace_substring(string, substring, replacement):
    new_string = string.replace(substring, replacement)
    return new_string

# Example usage
original_string = "The quick brown fox jumps over the lazy dog"
new_string = replace_substring(original_string, "quick", "slow")

print("Original string:", original_string)
print("New string:", new_string)