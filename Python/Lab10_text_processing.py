print("======================================")
print("         TEXT PROCESSING TOOL")
print("======================================")

# 1. Accept a sentence from the user
sentence = input("Enter a sentence: ")

print("\n--- Processing Results ---")

# 2. Display a character at a specific position using string indexing
index = int(input("Enter position for indexing: "))
print("Character at position", index, ": '" + sentence[index] + "'")

# 3. Extract a portion of the sentence using string slicing
start = int(input("Enter start index for slicing: "))
end = int(input("Enter end index for slicing : "))
print("Sliced string [" + str(start) + ":" + str(end) + "]    : '" + sentence[start:end] + "'")

# 4 & 5. Convert the sentence into uppercase and lowercase
print("Uppercase              :", sentence.upper())
print("Lowercase              :", sentence.lower())

# 6. Replace a specified word with another word
word_to_replace = input("Enter word to replace  : ")
replacement_word = input("Enter replacement word : ")
print("After replace          :", sentence.replace(word_to_replace, replacement_word))

# 7. Find and display the length of the sentence
print("Length of sentence     :", len(sentence))

print("======================================")
print("Analysis Complete!")
print("======================================")