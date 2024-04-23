# Binary search

import random

# lis = sorted([random.randint(-100, 100) for x in range(10)])

def binsearch_rek(lis, ele, steps=1):
    mid_idx = len(lis) // 2

    if lis[mid_idx] == ele:
        print(lis[mid_idx], 'gefunden! Steps=', steps)
    
    elif lis[mid_idx] < ele:
        lis = lis[mid_idx:]
        binsearch_rek(lis, ele, steps+1)

    elif lis[mid_idx] > ele:
        lis = lis[:mid_idx]
        binsearch_rek(lis, ele, steps+1)

# An welcher Position befindet sich ele
def binsearch(lis, ele, steps=1):
    low = 0
    high = len(lis) -1

    while low <= high:
        mid = (low + high) // 2
        guess = lis[mid]

        if guess == ele:
            return mid, steps
        
        elif guess > ele:
            high = mid -1
            steps += 1
        else: #lis[mid < ele]
            low = mid +1
            steps += 1

    return None

def main():
    lis = sorted(random.sample(range(50), 50))
    print(lis)

    lis = [1, 3, 5, 7, 9]
    # binsearch_rek(lis, 25)
    erg = binsearch(lis, 9)
    print(erg)


if __name__ == '__main__':
    main()