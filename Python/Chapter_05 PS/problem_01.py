# Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up!

hindi_words_dict = {
    "namaste": "hello",
    "dhanyawad": "thank you",
    "kripya": "please",
    "haan": "yes",
    "naa": "no",
    "kya": "what",
    "kaise": "how",
    "kab": "when",
    "kahan": "where",
    "kyun": "why",
}

word = input("Enter a Hindi word:")

print("English meaning :", hindi_words_dict.get(word,"word is not in dictionary"))
