from pecon import stats
import numpy as np

x = [2, 4, 6, 8]
xx = [2, 4, 6, 8, 10, 17, 24]
y = [1, 6, 12, 30, 17, 55, 40]
a = [1,2,3]
b = [1,5,7]

m = stats.mean(x)
v = stats.var(xx, ddof=1)
s = stats.std(a, ddof=1)
sb = stats.std(b, ddof=1)
c = stats.cov(xx, y, ddof=1)
r = stats.corr(xx, y)

print(f"mean = {m}\n var = {v}\n std = {s}\n stdb = {sb}\n cov = {c}")
print(f"r = {r.r} p = {r.pvalue}")
