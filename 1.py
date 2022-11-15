# import library random (to make random meanings)
import random

# create words bank
words_bank = ['автострада', 'бензин', 'инопланетянин',
              'самолет', 'библиотека', 'шайба',
              'олимпиада']

# create new variables
secret_word = random.choice(words_bank)

gamer_word = ['*'] * len(secret_word)
print(''.join(gamer_word))

# create and reset the variable
errors_cnt = 0

# create 'while' cycle
while True:
    letter = input('введите ОДНУ русскую букву: ').lower()
    if len(letter) != 1:
        continue

    if letter in secret_word:
        for idx, symbol in enumerate(secret_word):
            if symbol == letter:
                gamer_word[idx] = letter

        if '*' not in gamer_word:
            print('вы выиграли')
            break
    else:
        errors_cnt += 1
        print('ошибок допущено:', errors_cnt)

        if errors_cnt == 8:
            print('вы проиграли')
            break

    # output gamer word
    print(''.join(gamer_word))
