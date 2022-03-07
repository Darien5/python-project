"""Implementations of some sorting"""
import random


def merge(a0,a1):
    # todo
    d = []
    while len(a0) != 0 and len(a1) != 0:
        if a0[0] < a1[0]:
            d.append(a0[0])
            a0.remove(a0[0])

        else:
            d.append(a1[0])
            a1.remove(a1[0])

    if len(a0) == 0:
        d += a1
    else:
        d += a0

    return d

    #pass

def merge_sort(a):
    # todo
    if len(a) <= 1:
        return a
    else:
        s = len(a)//2
        a0 = merge_sort(a[:s])
        a1 = merge_sort(a[s:])

        return merge(a0,a1)


    #pass


def _quick_sort(a, i, n):
    # todo
    if n <= 1:
        return
    x = a[i + random.randint(1, n-1)]
    (r,j,q) = (i - 1,i,i + n)

    while j < q:
        if a[j] < x:
            r += 1
            a[j], a[p] = a[r], a[j]
            j += 1

        elif a[j] > x:
            q -= 1
            a[j], a[q] = a[q], a[j]

        else:
            j += 1

    _quick_sort(a,i,r - i + 1)
    _quick_sort(a,q,n - (q - i))
    #pass


def quick_sort(a):
    _quick_sort(a, 0, len(a))

    return a


def binary_search(a,x):
    l = 0
    p = len(a) - 1
    while p > 1:
        s = (p + 1)//2
        if x <= a[s]:
            p = s
        else:
            l = s + 1

    if a[l] == x:
        return l

    else:
        return "DNE"
