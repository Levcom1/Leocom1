import random

words_bank = ['автострада', 'бензин', 'инопланетянин',
              'самолёт', 'библиотека', 'шайба',
              'олимпиада']

secret_word = random.choice(words_bank)
print(secret_word)

gamer_word = ['*'] * len(secret_word)
print(''.join(gamer_word))

gamer_word[3] = 'г' # setter for str? -> immutable (mutable)
# immutable -> mutable: list
print(gamer_word)
