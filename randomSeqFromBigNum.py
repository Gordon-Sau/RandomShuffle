import random

def shuffle(seq):
    n = len(seq)
    fact = factorial(n)
    r = random.randrange(0, fact[-1])
    # Fisher–Yates shuffle algorithm
    for i in range(n-1, 0, -1):
        j, r = divmod(r, fact[i - 1])        
        swap(seq, j, i)
    return seq

def factorial(n):
    assert n > 0
    ret = [1]
    for i in range(2, n+1):
        ret.append(ret[-1] * i)
    return ret

def swap(seq, i, j):
    seq[i], seq[j] = seq[j], seq[i]

if __name__ == "__main__":
    print(shuffle(list(range(10))))
