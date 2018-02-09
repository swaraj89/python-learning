vowels=set('aeiou')
word=input('Enter name to see vowels:')

found = vowels.intersection(set(word))

for ch in sorted(found):
    print(ch)
