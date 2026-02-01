from pecon import stats
import numpy as np

x = np.array([1.28000000e002, 3.27670000e004, 8.38822400e006, 3.13740168e057, 1.12357916e164 ])
y = np.array([2.800000e002, 37.000e004, 2.2400e006, 3.740168e057, 1.357916e164 ])

m = stats.mean(x)
v = stats.var(x)
s = stats.std(x)
c = stats.cov(x, y)


print(f"mean = {m}\n var = {v}\n std = {s}\n cov = {c}")
