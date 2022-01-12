import random

def shuffle(seq):
    n = len(seq)
    # Fisher–Yates shuffle algorithm
    for i in range(n-1, 0, -1):
        j = random.randint(0, i)
        swap(seq, j, i)
    return seq

def swap(seq, i, j):
    seq[i], seq[j] = seq[j], seq[i]

if __name__ == "__main__":
    print(shuffle(list(range(5))))
