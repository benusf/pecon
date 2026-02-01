from .basic_stats import _mean, _var, _std, _cov, _corr




def mean(x, 
         drop_nan=False):
    """
    Compute arithmetic mean.

    Parameters
    ----------
    x : array-like

    Return
    ----------
    m : 
    """
    # xp = array_namespace(x)
    # x = _check_array(x, xp=xp, drop_nan=drop_nan)

    m = _mean(x)

    return m

def var(x):
    """
    Compute arithmetic mean.

    Parameters
    ----------
    x : array-like

    Return
    ----------
    m : 
    """
    var = _var(x)

    return var

def std(x):
    """
    Compute arithmetic mean.

    Parameters
    ----------
    x : array-like

    Return
    ----------
    m : 
    """
    std = _std(x)

    return std

def cov(x, y):
    """
    Compute arithmetic correlation.

    Parameters
    ----------
    x : array-like
    y : array-like
     
    Return
    ----------
    r :
    p : 
    """
    if len(x) != len(y):
        msg = "x and y must have same lenght"
        raise ValueError(msg)
    cov = _cov(x,y)

    return cov

def corr(x, y):
    """
    Compute arithmetic correlation.

    Parameters
    ----------
    x : array-like
    y : array-like
     
    Return
    ----------
    r :
    p : 
    """
    r, p = _corr(x,y)

    return r, p
