# read a text file and display the number of vowels/consonants/uppercase/lowercase chars in file
# Credits: Dhruv , XII-D

def count_chars(file_path):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    upper_count = 0
    lower_count = 0
    vowel_count = 0
    consonant_count = 0

    with open(file_path, "r") as file:
        data = file.read()
        for char in data:
            if char.isupper():
                upper_count += 1
            elif char.islower():
                lower_count += 1
            if char in vowels:
                vowel_count += 1
            elif char in consonants:
                consonant_count += 1

    print("Number of vowels:", vowel_count)
    print("Number of consonants:", consonant_count)
    print("Number of uppercase characters:", upper_count)
    print("Number of lowercase characters:", lower_count)


# Example usage
file_path = "example.txt"
count_chars(file_path)