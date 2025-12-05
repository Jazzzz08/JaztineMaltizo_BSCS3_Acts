# Task 3.2: Word Frequency Counter

text = input("Enter text (2–3 sentences): ").lower()
words = text.split()

freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)

print("\nWord Frequencies (Descending):")
for word, count in sorted_words:
    print(f"{word}: {count}")

most_common = sorted_words[0]
print(f"\nMost common word: '{most_common[0]}' ({most_common[1]} times)")
