import random

target = "I never go back on my word, because that is my Ninja way."
characters = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.',?!"


def makeList():
    charList = [random.choice(characters) for i in range(len(target))]
    return charList


def score(myList):
    matches = 0
    for i in range(len(target)):
        if myList[i] == target[i]:
            matches += 1
    return matches


def mutate(mylist):
    newlist = list(mylist)
    new_letter = random.choice(characters)
    index = random.randint(0, len(target) - 1)
    newlist[index] = new_letter
    return newlist


random.seed()
bestList = makeList()
bestScore = score(bestList)

guesses = 0
improvements = 0

while True:
    guess = mutate(bestList)
    guessScore = score(guess)
    guesses += 1

    if guessScore <= bestScore:
        continue
    print(''.join(guess), guessScore, guesses)
    if guessScore == len(target):
        break
    bestList = list(guess)
    bestScore = guessScore
