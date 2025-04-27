📚 Verificador de Vogais em Palavras (Python)
📝 Descrição
Este é um simples script Python que percorre uma lista de palavras e exibe, para cada uma, quais vogais ela contém.
Ideal para quem está começando a praticar laços (for) e manipulação de strings.

📚 Vowel Checker in Words (Python)
📝 Description
This is a simple Python script that loops through a list of words and shows, for each one, which vowels it contains.
Perfect for beginners practicing loops (for) and string handling.

🔥 Código / Code
python
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
            
⚙️ Como Usar / How to Use
Copie o código acima em um arquivo .py.

Execute o arquivo com Python 3.

Veja as vogais sendo listadas para cada palavra!

🚀 Habilidades Praticadas / Skills Practiced
Laços for

Estruturas de dados (tupla)

Manipulação de strings

Impressão formatada (f-string)

