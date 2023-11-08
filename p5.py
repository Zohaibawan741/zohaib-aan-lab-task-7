word = input("Enter a word: ")

vowels = "aeiou"
vowel_count = 0
consonant_count = 0

for letter in word:
    if letter.isalpha():
        if letter in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print(f"Vowels: {vowel_count}")
print(f"Consonants: {consonant_count}")
