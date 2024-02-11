with open("books/frankenstein.txt", "r") as f:
    data = f.read()

words = data.split()
char_freq = {}
for c in data:
    _c = c.lower()
    if _c not in char_freq:
        char_freq[_c] = 0
    char_freq[_c] += 1
print("--- Begin report of books/frankenstein.txt ---")
print(f"{len(words)} words found in the document")
print("")
for char, freq in char_freq.items():
    if not char.isalpha():
        continue
    print(f"The '{char}' character was found {freq} times")
print("--- End report ---")