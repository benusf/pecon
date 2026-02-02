from .basic_stats import _mean, _var, _std, _cov, _corr



def mean(x, drop_nan=False):
    """
    Compute the arithmetic mean.

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

def var(x):
    """
    Compute variance

    Parameters
    ----------
    x : array-like

    Return
    ----------
    var : float
        variance of the array
    """
    var = _var(x)

    return var

def std(x):
    """
    Compute standard deviation

    Parameters
    ----------
    x : array-like

    Return
    ----------
    std : float
        standard deviation of the array
    """
    std = _std(x)

    return std

def cov(x, y):
    """
    Compute covariance between two variable

    Parameters
    ----------
    x : array-like
    y : array-like
     
    Return
    ----------
    cov : float
        the covariance of the x and y.
    """
    if len(x) != len(y):
        msg = "x and y must have same lenght"
        raise ValueError(msg)
    cov = _cov(x,y)

    return cov

def corr(x, y):
    """
    Compute arithmetic correlation

    Parameters
    ----------
    x : array-like
    y : array-like
     
    Return
    ----------
    r : float
        correlation coeficient
    p : float
        p-value
    
    Example
    ----------
    >>from pecon import stats

    >>x = [1, 3, 5, 7]
    >>y = [12, 5, 64 43]

    >>r, p = stats.corr(x, y)
    >>print(f"Correlation Coeficient = {r} and pvalue = {p}")
    """
    r, p = _corr(x,y)

    return r, p
