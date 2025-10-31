import random
name=input("What is your name?")
print("Good Luck!",name)
words=['rainbow','computer','science',
       'programming','python','hello',
       'condition','logic','newspaper']
word=random.choice(words)
print("Guess the characters")
guesses=''
turns=12
while turns>0:
    failed=0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            failed+=1
    if failed==0:
        print("You WIN!")
        print("The word is:",word)
        break
    print()
    guess=input("Guess a character:")
    guesses+=guess
    if guess not in word:
        turns-=1
        print("WRONG!")
        print("You have",+turns,'more guesses')
        if turns==0:
            print("You LOSE!!!")
            print("the word was",word)
