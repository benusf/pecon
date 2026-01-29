# distutils: language = c
from pecon.stats.basic_stats import correlation, mean

# Mean func

cpdef mean(list x):
    return mean(x)

# correlation func

cpdef tuple corr(list x, list y):
    return correlation(x, y)
