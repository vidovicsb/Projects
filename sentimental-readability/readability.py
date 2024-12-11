from cs50 import get_string

text = get_string("Text: ")

sentences = 0
letters = 0

for c in text:
    if c == "." or c == "?" or c == "!":
        sentences += 1
    elif (ord(c) >= 65 and ord(c) <= 90) or (ord(c) >= 97 and ord(c) <= 122):
        letters += 1

list = text.split(" ")
words = len(list)

L = (letters * 100) / words
S = (sentences * 100) / words

grade = round(0.0588 * L - 0.296 * S - 15.8)


if grade >= 16:
    print("Grade: 16+")
elif grade < 1:
    print("Before Grade 1")
else:
    print(f"Grade {grade}")

