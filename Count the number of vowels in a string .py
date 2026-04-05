
# This program counts the number of vowels in a sentence

# Ask the user to enter a sentence
text = input("Enter a sentence: ")

# Define the vowels
vowels = "aeiou"

# Initialize a counter to 0
count = 0

# Loop through each character in the text
for char in text.lower():  # Convert to lowercase for easy comparison
    # Check if the character is a vowel
    if char in vowels:
        count += 1  # Increase count if vowel is found

# Display the total number of vowels
print("Number of vowels:", count)
