from pecon import stats

x = [8.38822400e006, 4, 9.38844338e0545, 8, 10, 12, 43, 132, 65, 12]
y = [1, 3, 5, 7, 9, 10, 20, 32, 1234, 20]


mx = stats.mean(x)
my = stats.mean(y)

coef, pvalue = stats.corr(x, y)

print(f"X mean = {mx} and Y mean = {my}\n")
print(f"Correlation coef = {coef}\npvalue = {pvalue}")
