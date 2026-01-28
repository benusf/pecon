# distutils: language = c
from pecon.stats.basic_stats import correlation

# Mean func

cpdef mean(list x):
    cdef int n = len(x)
    cdef double total = 0.0
    cdef int i

    for i in range(n):
        total += x[i]

    return total / n

# correlation func

cpdef tuple corr(list x, list y):
    return correlation(x, y)
