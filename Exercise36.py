vowel=['a','e','i','o','u']
letter=input('Enter the letter: ')
if letter in vowel:
    print('letter is a vowel')
elif letter == 'y':
    print('sometimes y is a vowel, and sometimes y is a consonant')
else:
    print('letter is a consonant')