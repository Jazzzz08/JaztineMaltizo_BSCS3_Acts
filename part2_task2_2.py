# Task 2.2: Unique Word Counter with Sets

text = input("Enter a sample text (at least 3 sentences): ").lower()
words = text.split()
unique_words = set(words)

print(f"\nTotal words: {len(words)}")
print(f"Unique words: {len(unique_words)}")

# Word frequency
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print("\nWord Frequencies:")
for w, c in word_count.items():
    print(f"{w}: {c}")

most_common = max(word_count, key=word_count.get)
print(f"\nMost common word: '{most_common}' ({word_count[most_common]} times)")
