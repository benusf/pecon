from pecon import stats


# def test_mean():
#     x = [2, 4, 6, 8, 10]
#     y = [1, 3, 5, 7, 9]

#     mx = stats.mean(x)
#     my = stats.mean(y)
#     assert mx == 6 and my == 5


def test_corr():
    x = [2, 4, 6, 8]
    y = [1, 3, 5, 7]

    coef, pvalue = stats.corr(x, y)

    assert coef == 1
