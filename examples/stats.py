from pecon import stats, OLS
import numpy as np

x = [2, 4, 6, 8]
c = np.array([2, 4, 6, 8])
xx = [2, 4, 6, 8, 10, 17, 24]
y = [1, 6, 12, 30, 17, 55, 40]
a = np.array([[1,2,3],
     [6,7,34]])
b = [1,5,2, 7]

m = stats.mean(c, allow_nan=False)
# v = stats.var(xx, ddof=1)
# s = stats.std(a, ddof=1)
# sb = stats.std(b, ddof=1)
# c = stats.cov(xx, y, ddof=1)
# r = stats.corr(xx, y)
# print(f"r = {r.r} p = {r.pvalue}")

e = OLS(x, b)
e.fit()
e.summary()
print(f"mean = {m}\n")
