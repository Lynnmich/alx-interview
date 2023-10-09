#!/usr/bin/python3
''' Prime Game Module '''


def rwh_primes(n):
    '''
    method
    '''
    sieve = [True] * n
    for i in range(3, int(n**0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * int((n - i * i - 1) / (2 * i) + 1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


def playMatch(n):
    ''' plays a single round '''
    primes = rwh_primes(n + 1)
    return 1 - (len(primes) % 2) if n > 1 else 1


def isWinner(x, nums):
    ''' plays the whole game '''
    if type(x) is not int or x < 1:
        return None
    players = {0: 'Maria', 1: 'Ben'}
    wins = {0: 0, 1: 0}
    for num in nums:
        wins[playMatch(num)] += 1
    return (None if wins[0] == wins[1]
            else players[0] if wins[0] > wins[1]
            else players[1])
