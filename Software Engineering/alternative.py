
# alternative.py
# ---Task 1: Alternate characters---
text = input("Enter a string: ")

# Create a new string with alternating uppercase/lowercase characters
result_chars = ""  # Fixed: initialize the correct variable
for i, char in enumerate(text):
    if i % 2 == 0:
        result_chars += char.upper()
    else:
        result_chars += char.lower()

print("Alternate character:", result_chars)

# ---Task 2: Alternate words---

# Split words into a list
words = text.split()

# Change case of every alternate word
for i in range(len(words)):
    if i % 2 == 0:
        words[i] = words[i].lower()
    else:
        words[i] = words[i].upper()

# Join back into a sentence
result_words = " ".join(words)
print("Alternate words:", result_words)
