# Exercise 1


def mySum(num):
    return sum([i for i in range(1,num+1)])


def mySum2(num):
    return sum([i**2 + 1 for i in range(1, num+1)])

# Exercise 2


def average3(numList):
    return sum(numList)/len(numList)


print(average3([53, 28, 54, 84, 65, 60, 22, 93, 62, 27, 16, 25, 74, 42, 4, 42,
15, 96, 11, 70, 83, 97, 75]))