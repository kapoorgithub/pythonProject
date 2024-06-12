# Define a function called is_vowel that takes one parameter: char (a character).
def is_vowel(char):
    # Define a string called all_vowels containing all lowercase vowel characters.
    all_vowels = 'aeiou'

    # Check if the input character (char) is present in the all_vowels string.
    return char in all_vowels

# Call the is_vowel function with two different characters and print the results.
print(is_vowel('c'))  # Output: False (character 'c' is not a vowel)
print(is_vowel('e'))  # Output: True (character 'e' is a vowel)
