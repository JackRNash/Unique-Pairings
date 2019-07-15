import numpy as np


def generator(n, letters=True):
    """
    n - Number of people
    letters - If true, letters will be used to represent people, otherwise numbers will be used
    """
    ppl = list(range(1, n))
    if letters:
        for i in range(n - 1):
            ppl[i] = chr(ppl[i] + 65)
    while True:
        for i in ppl:
            yield i


def make_matchings(n, letters=True):
    """
    n - Number of people. Should be even, if not, will make an extra dummy spot and the person matched w/ it will
    sit out each round
    letters - If true, letters will be used to represent people, otherwise numbers will be used
    """
    # Fix even
    if n % 2 is not 0:
        n += 1

    # Create arrays. The ith row represents the ith round
    if letters:
        matchings = np.chararray((n - 1, n), unicode=True)
    else:
        matchings = np.ndarray((n - 1, n), dtype=np.int16)

    person = generator(n, letters)

    # Create each round's order by holding the first person fixed and cycling everybody else over one
    # from where they were last round
    for i in range(0, n - 1):
        for j in range(1, n):
            matchings[i, j] = next(person)
        next(person)
    for i in range(n - 1):
        if letters:
            matchings[i, 0] = 'A'
        else:
            matchings[i, 0] = 0

    # Print. People across from one another are paired together
    for i in range(n - 1):
        print('Round', i + 1)
        line1 = ''
        line2 = ''
        if not letters:
            for j in range(int(n / 2)):
                line1 += str(int(matchings[i, j])) + ' '
            for j in range(n - 1, int(n / 2) - 1, -1):
                line2 += str(int(matchings[i, j])) + ' '
        else:
            for j in range(int(n / 2)):
                line1 += str(matchings[i, j]) + ' '
            for j in range(n - 1, int(n / 2) - 1, -1):
                line2 += str(matchings[i, j]) + ' '
        print(line1 + '\n' + line2)
        print()
        print()

    return matchings


make_matchings(10)
