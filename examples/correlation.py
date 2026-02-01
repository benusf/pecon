from pecon import stats

x = [2, 4, 6, 8]
y = [1, 3, 5, 7]


mx = stats.mean(x)
my = stats.mean(y)

coef, pvalue = stats.corr(x, y)

print(f"X mean = {mx} and Y mean = {my}\n")
print(f"Correlation coef = {coef}\npvalue = {pvalue}")
