from .basic_stats import _mean, _var, _std, _cov, _corr
from dataclasses import dataclass

"""
Statistical utility functions for data analysis.

The ``stats`` module implements core descriptive statistics such as
mean, variance, standard deviation, covariance, and correlation.
It is designed for clarity, numerical stability, and seamless use
in econometric and scientific applications.
"""

@dataclass
class CorrResult:
    r: float        # correlation coefficient
    pvalue: float   # p-value
    tstat: float    # t-statistic


def mean(x, drop_nan=False):
    """
    Compute the arithmetic mean of a dataset.

    The mean is the sum of all observations divided by the number of observations.
    It provides a measure of the central tendency of the data.

    Parameters
    ----------
    x : array-like
        Input data.

    Returns
    -------
    float
        The mean of the input values.

    Examples
    --------
    >>> from pecon import stats
    >>> x = [2, 4, 6, 8]
    >>> y = [1, 3, 5, 7]
    >>> mx = stats.mean(x)
    >>> my = stats.mean(y)
    >>> print(f"X mean = {mx} and Y mean = {my}")
    X mean = 5.0 and Y mean = 4.0

    """

    # xp = array_namespace(x)
    # x = _check_array(x, xp=xp, drop_nan=drop_nan)

    m = _mean(x)
    return m

def var(x, ddof=1):
    """
    Compute the variance of a dataset.

    Variance measures the average squared deviation of observations
    from their mean, indicating the dispersion of the data.

    Parameters
    ----------
    x : array-like
        One-dimensional sequence of numerical values.
    ddof : int, optional
        Delta degrees of freedom. The divisor used is (N - ddof).
        Use ddof=0 for population variance and ddof=1 for sample variance.

    Returns
    -------
    float
        The variance of the data.

    Notes
    -----
    The value of `ddof` must satisfy 0 <= ddof < N, where N is
    the number of observations. Otherwise, a ValueError is raised.

    Examples
    --------
    >>> from pecon import stats
    >>> x = [2, 4, 6, 8]
    >>> var = stats.var(x, ddof=1)
    >>> print(f"Var = {var}")
    Var = 6.666666666666667

    """

    if not isinstance(ddof, int):
        raise TypeError("ddof must be an integer")

    if ddof < 0:
        raise ValueError("ddof must be non-negative")

    if ddof >= len(x):
        raise ValueError(
            "ddof must be less than the number of observations")
    var = _var(x, ddof=ddof)

    return var

def std(x, ddof=1):
    """
    Compute the standard deviation of a dataset.

    The standard deviation is the square root of the variance and
    represents dispersion in the same units as the original data.

    Parameters
    ----------
    x : array-like
        One-dimensional sequence of numerical values.
    ddof : int, optional
        Delta degrees of freedom. Use ddof=0 for population
        standard deviation and ddof=1 for sample standard deviation.

    Returns
    -------
    float
        The standard deviation of the data.

    Notes
    -----
    The value of `ddof` must satisfy 0 <= ddof < N, where N is
    the number of observations. Otherwise, a ValueError is raised.

    Examples
    --------
    >>> from pecon import stats
    >>> x = [2, 4, 6, 8]
    >>> std = stats.std(x, ddof=1)
    >>> print(f"std = {var}")
    std = 2.581988897471611
    
    """

    if not isinstance(ddof, int):
        raise TypeError("ddof must be an integer")

    if ddof < 0:
        raise ValueError("ddof must be non-negative")

    if ddof >= len(x):
        raise ValueError("ddof must be less than the number of observations")

    std = _std(x, ddof=ddof)

    return std

def cov(x, y, ddof=1):
    """
    Compute the covariance between two variables.

    Covariance measures the direction of the linear relationship
    between two variables. A positive value indicates that the
    variables tend to move together, while a negative value
    indicates an inverse relationship.

    Parameters
    ----------
    x, y : array-like
        One-dimensional sequences of numerical values with equal length.
    ddof : int, optional
        Delta degrees of freedom. Default is 1 for sample covariance.

    Returns
    -------
    float
        The covariance between x and y.

    Notes
    -----
    The value of `ddof` must satisfy 0 <= ddof < N, where N is
    the number of observations. Otherwise, a ValueError is raised.

    Examples
    --------
    >>> from pecon import stats
    >>> x = [2, 4, 6, 8, 10, 17, 24]
    >>> y = [1, 6, 12, 30, 17, 55, 40]
    >>> cov = stats.cov(x, y, ddof=1)
    >>> print(f"Covariance = {cov}")
    Covariance = 128.33333333333337

    """

    if not isinstance(ddof, int):
        raise TypeError("ddof must be an integer")

    if ddof < 0:
        raise ValueError("ddof must be non-negative")

    if ddof >= len(x):
        raise ValueError("ddof must be less than the number of observations")
    dof = ddof
    cov = _cov(x,y, dof)

    return cov

def corr(x, y) -> CorrResult:
    """
    Compute the Pearson correlation coefficient between two variables.

    The correlation coefficient measures the strength and direction
    of a linear relationship between two variables. Its value lies
    between -1 and 1.

    Parameters
    ----------
    x : array-like
        One-dimensional sequence of numerical values.
    y : array-like
        One-dimensional sequence of numerical values of the same length as x.

    Returns
    -------
    CorrResult
        Dataclass containing:
            - r : float
                Pearson correlation coefficient.
            - pvalue : float
                Two-tailed p-value for testing non-correlation.
            - tstat : float
                t-statistic corresponding to the correlation.

    Notes
    -----
    A value of 1 indicates perfect positive correlation,
    -1 indicates perfect negative correlation,
    and 0 indicates no linear correlation.

    Examples
    --------
    >>> from pecon import stats
    >>> x = [2, 4, 6, 8, 10, 17, 24]
    >>> y = [1, 6, 12, 30, 17, 55, 40]
    >>> res = stats.corr(x, y)
    >>> print(f"Correlation Coefficient = {res.r}\\n pvalue = {res.pvalue}")
    Correlation Coefficient = 0.8420191952099748
    pvalue = 0.01746558746945201

    """

    r, p, t = _corr(x, y)

    return CorrResult(r, p, t)
