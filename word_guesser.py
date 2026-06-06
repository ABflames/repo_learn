import random
word_bank = ['apple','table','chair','bread','plant']
word = random.choice(word_bank)

guessedWord = ['_'] * len(word)

attempts = 10

while attempts > 0:
    print('\nCurrent word: ' + ' '.join(guessedWord))
    guess = input('Enter a letter: ').lower()
    
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessedWord[i] = guess
        print('Yay! Great guess!')
        
    else:
        attempts -= 1
        print('Nope!Try again. Attempts left:' + str(attempts))
        
    if '_' not in guessedWord:
        print('\n Congrats! U guessed the right word: ' + word)
        break
    
if attempts == 0 and '_' in guessedWord:
    print('\n Sorry! U ran out of attempts. The word was: ' + word)