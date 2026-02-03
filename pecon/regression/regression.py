from pecon.stats import cov, var, mean 
from ._regression import _OLS
import numpy as np

class OLS:
    """
    Simple Ordinary Least Squares (OLS) regression for a single independent variable.

    This class implements simple linear regression with one predictor (x) and one dependent variable (y).
    It calculates the slope (beta) and intercept (alpha) using the classical OLS formulas:

    .. math::

       \\beta = \\frac{\\sum (x - \\bar{x}) (y - \\bar{y})}{\\sum (x - \\bar{x})^2}

    .. math::

       \\alpha = \\bar{y} - \\beta \\bar{x}

    Attributes
    ----------
        x : array-like
            The independent variable (predictor). Must be 1-dimensional.
        y : array-like
            The dependent variable (response). Must be 1-dimensional.
        beta : float
            Estimated slope of the regression line. Calculated after calling `fit()`.
        alpha : float
            Estimated intercept of the regression line. Calculated after calling `fit()`.
        r : float
            Sample correlation coefficient between x and y.
        p : float
            Two-tailed p-value for testing non-correlation between x and y.
        fitted : bool
            Flag indicating whether the model has been fitted.

    Raises
    ------
        ValueError
            If x or y are not 1-dimensional arrays of the same length.
        Warning
            Warns if the independent variable has zero variance, which makes beta undefined.

    Example
    -------
    >>> import numpy as np
    >>> from simple_ols import SimpleOLS
    >>> x = np.array([2, 4, 6, 8])
    >>> y = np.array([1, 5, 2, 7])
    >>> model = SimpleOLS(x, y)
    >>> model.fit()
    >>> model.summary()
    beta  = 0.75
    alpha = 0.0
    r     = 0.408
    p     = 0.6
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.beta = None
        self.alpha = None
        self.r = None
        self.p = None
        self.fitted = False
        self.onedim = False


    def fit(self):
        """
        Fit the Ordinary Least Squares (OLS) model.

        Computes the slope (beta) and intercept (alpha) of the regression
        line using the closed-form OLS solution. Also computes the sample
        correlation coefficient and its two-tailed p-value.

        Notes
        -----
        The estimates are given by:

        .. math::

            \\beta = \\frac{\\sum (x - \\bar{x})(y - \\bar{y})}
                          {\\sum (x - \\bar{x})^2}

            \\alpha = \\bar{y} - \\beta \\bar{x}

        After calling this method, the following attributes are available:

        - ``beta`` : slope coefficient
        - ``alpha`` : intercept
        - ``r`` : correlation coefficient
        - ``p`` : p-value for testing non-correlation
        - ``fitted`` : set to ``True``

        Raises
        ------
        ValueError
            If the independent variable has zero variance.
        """
        arr = np.asarray(self.x)
        if arr.ndim == 1:
            self.onedim = True
            self.alpha, self.beta, self.r, self.p = _OLS(self.x, self.y, self.onedim)
        else:
            pass 

        self.fitted = True


    def summary(self):
        """
        Print a summary of the fitted OLS regression.

        Displays the estimated coefficients and correlation statistics in
        a human-readable format. This method requires the model to be
        fitted first.

        Output
        ------
        beta
            Estimated slope coefficient.
        alpha
            Estimated intercept.
        r
            Sample correlation coefficient.
        p
            Two-tailed p-value for testing non-correlation.

        Raises
        ------
        RuntimeError
            If the model has not been fitted. Call ``fit()`` first.
        """
        if not self.fitted:
            raise RuntimeError("Model must be fitted before calling summary().")

        if self.onedim:
            print("OLS Regression Results")
            print("----------------------")
            print(f"alpha  = {self.alpha}")
            print(f"beta  = {self.beta}")
            print(f"Rsquare  = {self.r}")
            print(f"pvalue  = {self.p}")
        else:
            msg = "multi regression not implemented yet"
            raise ValueError(msg)
