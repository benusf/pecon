import numpy as numpy
from numpy.testing import assert_array_equal
import math
import pytest
from pytest import raises as assert_raises

from pecon import stats
from pecon.stats import mean, var, std, cov, corr


def test_mean_list():
    assert mean([1, 2, 3]) == 2.0

def test_mean_memoryview():
    import array
    x = array.array("d", [2.0, 4.0, 6.0])
    assert mean(x) == 4.0

def test_mean_empty_list():
    with pytest.raises(ValueError):
        mean([])

def test_mean_empty_array():
    import array
    x = array.array("d")
    with pytest.raises(ValueError):
        mean(x)
def test_mean_empty_numpy():
    import numpy as np
    with pytest.raises(ValueError):
        mean(np.array([]))

def test_var_basic():
    assert var([1, 2, 3]) == pytest.approx(2/(3-1))

def test_var_constant():
    assert var([5, 5, 5]) == 0.0

def test_var_float():
    assert var([1.0, 2.0, 4.0]) == pytest.approx(2.333333)

def test_var_array():
    import array
    x = array.array("d", [1, 2, 3])
    assert var(x) == pytest.approx(2/(3-1))

def test_var_empty():
    with pytest.raises(ValueError):
        var([])

def test_var_single_value():
    with pytest.raises(ValueError):
        var([1])

def test_std_basic():
    assert std([1, 2, 3]) == pytest.approx(math.sqrt(2/(3-1)))

def test_std_constant():
    assert std([5, 5, 5]) == 0.0

def test_std_array():
    import array
    x = array.array("d", [1, 2, 3])
    assert std(x) == pytest.approx(math.sqrt(2/(3-1)))

def test_std_empty():
    with pytest.raises(ValueError):
        std([])

def test_std_single_value():
    with pytest.raises(ValueError):
        std([42])

def test_cov_basic():
    x = [1, 2, 3]
    y = [1, 5, 7]
    # mean(x)=2, mean(y)=13/3
    # cov = ((-1)*(-10/3) + 0*(2/3) + 1*(8/3)) / 3 = 6/3 = 2
    assert cov(x, y, 0) == pytest.approx(2.0)

def test_cov_identical():
    x = [1, 2, 3]
    assert cov(x, x, 0) == pytest.approx(2/3)

def test_cov_negative():
    x = [1, 2, 3]
    y = [3, 2, 1]
    assert cov(x, y, 0) == pytest.approx(-2/3)

def test_cov_empty():
    with pytest.raises(ValueError):
        cov([], [], 0)

def test_cov_single():
    with pytest.raises(ValueError):
        cov([1], [1], 0)

def test_cov_mismatched_lengths():
    with pytest.raises(ValueError):
        cov([1, 2, 3], [1, 2], 0)

def test_cov_array():
    import array
    x = array.array("d", [1, 2, 3])
    y = array.array("d", [1, 5, 7])
    assert cov(x, y, 0) == pytest.approx(2.0)

def test_cov_numpy():
    import numpy as np
    x = np.array([1, 2, 3])
    y = np.array([1, 5, 7])
    assert cov(x, y, 0) == pytest.approx(np.cov(x, y, bias=True)[0, 1])

def test_corr():
    x = [2, 4, 6, 8]
    y = [1, 3, 5, 7]

    res = stats.corr(x, y)

    assert res.r == 1 and res.pvalue == 0.0
