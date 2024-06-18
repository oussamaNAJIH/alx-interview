#!/usr/bin/python3
"""
this module if for isWinner function
"""

def isWinner(x, nums):
    

def isWinner(x, nums):
    """
    Return: name of the player that won the most rounds
    """
    if x <= 0 or not nums:
        return None

    max_num = max(nums)
    
    # Step 1: Use Sieve of Eratosthenes to find all primes up to max_num
    sieve = [True] * (max_num + 1)
    sieve[0] = sieve[1] = False

    for start in range(2, int(max_num**0.5) + 1):
        if sieve[start]:
            for multiple in range(start*start, max_num + 1, start):
                sieve[multiple] = False

    primes = [num for num, is_prime in enumerate(sieve) if is_prime]
    
    def play_game(n):
        remaining = set(range(1, n + 1))
        turn = 0

        while True:
            move_made = False
            for prime in primes:
                if prime in remaining:
                    move_made = True
                    multiples = set(range(prime, n + 1, prime))
                    remaining -= multiples
                    break
            
            if not move_made:
                return 1 - turn
            
            turn = 1 - turn

    maria_wins = 0
    ben_wins = 0
    
    for num in nums:
        if num == 1:
            ben_wins += 1
        else:
            winner = play_game(num)
            if winner == 0:
                maria_wins += 1
            else:
                ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
