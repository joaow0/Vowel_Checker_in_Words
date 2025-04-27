words = ('learn', 'program', 'language', 'python',
         'course', 'free', 'study', 'practice',
         'work', 'market', 'programmer', 'future',
         'night', 'exercise', 'python', 'tuple', 'words',
         'vowels', 'romantic', 'grade', 'youtube', 'soapopera')

for word in words:
    print(f'\nIn the word {word} we have ', end='')
    for letter in word:
        if letter in 'aeiou':
            print(f'{letter}', end='')