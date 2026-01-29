from pecon import stats

x = [2,54, 4, 6, 8,4]
y = [1, 12,3, 5, 7,3]


# mx = stats.mean(x)
# my = stats.mean(y)

coef, pvalue = stats.corr(x, y)

# print(f"X mean = {mx} and Y mean = {my}\n")
print(f"Correlation coef = {coef}\npvalue = {pvalue}")
