import random

# Generere en tilfældig permutation af heltallene fra 0 til n-1 (n som input)

def randPermutation(n):
    
    # generate a range of numbers from start to stop
    numbers = list(range(0, n-1))

    # shuffle the numbers
    random.shuffle(numbers)
    print(numbers)

# lets test the code
randPermutation(10)
