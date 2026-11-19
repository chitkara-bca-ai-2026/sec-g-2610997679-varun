# Get input from the user
sentence = input("Enter a sentence: ")

# Initialize counters
vowels = 0
consonants = 0
digits = 0
spaces = 0
special_chars = 0

# Define vowels to check against
vowel_list = "aeiouAEIOU"

# Loop through each character in the sentence
for char in sentence:
    if char in vowel_list:
        vowels = vowels + 1
    elif char.isalpha():
        consonants = consonants + 1
    elif char.isdigit():
        digits = digits + 1
    elif char == " ":
        spaces = spaces + 1
    else:
        special_chars = special_chars + 1

# Calculate totals and percentages
total_chars = len(sentence)
words = len(sentence.split())
total_letters = vowels + consonants

# Prevent division by zero error if no letters are entered
if total_letters > 0:
    vowel_percent = (vowels / total_letters) * 100
else:
    vowel_percent = 0.0

# Print the final report
print("==========================================")
print("DOCUMENT ANALYSIS REPORT")
print("==========================================")
print("Sentence:", sentence)
print("Total characters:", total_chars)
print()
print("--- Character Breakdown ---")
print(f"Words:              {words}")
print(f"Vowels:             {vowels}")
print(f"Consonants:         {consonants}")
print(f"Digits:             {digits}")
print(f"Spaces:             {spaces}")
print(f"Special characters: {special_chars}")
print()
print("--- Summary ---")
print(f"Total letters:      {total_letters}")
print(f"Vowel percentage:   {vowel_percent:.1f}%")
print()
print("==========================================")
print("Analysis Complete!")
print("==========================================")