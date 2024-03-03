# All kod nedan är från numerize lib som är en modul fast den modulen går endast upp till T och mitt program kommer till större tal än detta. 
# Jag tog därför deras kod för att sedan "förbättra" den till min egna storlek på tal.
# https://en.wikipedia.org/wiki/Names_of_large_numbers

from decimal import Decimal

def round_num(n, decimals):
    '''
    Params:
    n - number to round
    decimals - number of decimal places to round to
    Round number to 2 decimal places
    For example:
    10.0 -> 10
    10.222 -> 10.22
    '''
    return n.to_integral() if n == n.to_integral() else round(n.normalize(), decimals)

def drop_zero(n):
    '''
    Drop trailing 0s
    For example:
    10.100 -> 10.1
    '''
    n = str(n)
    return n.rstrip('0').rstrip('.') if '.' in n else n

def numerize(n, decimals=2):
    '''
    Params:
    n - number to be numerized
    decimals - number of decimal places to round to
    Converts numbers like:
    1,000 -> 1K
    1,000,000 -> 1M
    1,000,000,000 -> 1B
    1,000,000,000,000 -> 1T
    '''

    n = abs(Decimal(n))
    if n < 1000:
        return str(drop_zero(round_num(n, decimals)))
    elif n >= 1000 and n < 1000000:
        if n % 1000 == 0:
            return str(int(n / 1000)) + " Thousand"
        else:
            n = n / 1000
            return str(drop_zero(round_num(n, decimals))) + " Thousand"
    elif n >= 1000000 and n < 1000000000:
        if n % 1000000 == 0:
            return str(int(n / 1000000)) + " Million"
        else:
            n = n / 1000000
            return str(drop_zero(round_num(n, decimals))) + " Million"
    elif n >= 1000000000 and n < 1000000000000:
        if n % 1000000000 == 0:
            return str(int(n / 1000000000)) + " Billion"
        else:
            n = n / 1000000000
            return str(drop_zero(round_num(n, decimals))) + " Billion"
    elif n >= 1000000000000 and n < 1000000000000000:
        if n % 1000000000000 == 0:
            return str(int(n / 1000000000000)) + " Trillion"
        else:
            n = n / 1000000000000
            return str(drop_zero(round_num(n, decimals))) + " Trillion"
    elif n >= 1000000000000000 and n < 1000000000000000000:
        if n %1000000000000000 == 0:
            return str(int(n / 1000000000000000)) + " Quadrillion"
        else:
            n = n / 1000000000000000
            return str(drop_zero(round_num(n, decimals))) + " Quadrillion"
    elif n >= 1000000000000000000 and n < 1000000000000000000000:
        if n % 1000000000000000000 == 0:
            return str(int(n / 1000000000000000000)) + " Quintillion"
        else:
            n = n / 1000000000000000000
            return str(drop_zero(round_num(n, decimals))) + " Quintillion"
    elif n >= 1000000000000000000000 and n < 1000000000000000000000000:
        if n % 1000000000000000000000 == 0:
            return str(int(n / 1000000000000000000000)) + " Sextillion"
        else:
            n = n / 1000000000000000000000
            return str(drop_zero(round_num(n, decimals))) + " Sextillion"
    elif n >= 1000000000000000000000000 and n < 1000000000000000000000000000:
        if n % 1000000000000000000000000 == 0:
          return str(int(n / 1000000000000000000000000)) + " Septendecillion"
        else:
          n = n / 1000000000000000000000000
          return str(drop_zero(round_num(n, decimals))) + " Septendecillion"
    elif n >= 1000000000000000000000000000 and n < 1000000000000000000000000000000:
        if n % 1000000000000000000000000000 == 0:
          return str(int(n / 1000000000000000000000000000)) + " Octodecillion"
        else:
          n = n / 1000000000000000000000000000
          return str(drop_zero(round_num(n, decimals))) + " Octodecillion"
    elif n >= 1000000000000000000000000000000 and n < 100000000000000000000000000000000:
        if n % 1000000000000000000000000000000 == 0:
          return str(int(n / 1000000000000000000000000000000)) + " Novemdecillion"
        else:
          n = n / 1000000000000000000000000000000
          return str(drop_zero(round_num(n, decimals))) + " Novemdecillion"
    elif n >= 100000000000000000000000000000000 and n < 100000000000000000000000000000000000:
        if n % 100000000000000000000000000000000 == 0:
            return str(int(n / 100000000000000000000000000000000)) + " Vigintillion"
        else:
          n = n / 100000000000000000000000000000000
          return str(drop_zero(round_num(n, decimals))) + " Vigintillion"
    elif n >= 100000000000000000000000000000000000:
        n = n / 100000000000000000000000000000000000
        return str(drop_zero(round_num(n, decimals))) + " Vigintillion"
    else:
        return str(n)