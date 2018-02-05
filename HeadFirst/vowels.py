vowels=['a', 'e', 'i', 'o', 'u']
word=input('Enter name to see vowels:')
found = []

for letter in word:
    if letter in vowels:
        found.append(letter)

count = len(found)
if  count > 0:
    print("No of vowels:", (count))
    for vowel in found:
        print(vowel)
else:
    print("No vowels")
