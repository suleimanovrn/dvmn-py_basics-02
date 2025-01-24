from transliterate import translit
from num2words import num2words
print(translit('''Ladies and gentlemen, I'm 78 years old and I finally got 15 minutes of fame once in a lifetime and I guess that this is mine. People have also told me to make these next few minutes escruciatingly embarrassing and to take vengeance of my enemies. Neither will happen.
More than 3 years ago I moved to Novo-Novsk, but worked on new Magnetic Storage for last 40. When I was 8...''', 'ru'))
numbers = (
    "78 - " + num2words(78, lang='en') + "\n" +
    "15 - " + num2words(15, lang='en') + "\n" +
    "3 - " + num2words(3, lang='en') + "\n" +
    "40 - " + num2words(40, lang='en') + "\n" +
    "8 - " + num2words(8, lang='en'))
print(translit(numbers, "ru"))
