"""
_pecon._backend._array_api_checks.py

Unified array validation for all backends: NumPy, CuPy, Torch, JAX, Dask.
"""

from pecon._backend._array_api import array_namespace, _asarray
import numpy as np

def _check_array(x, *, xp=None, allow_nan=True, allow_inf=False, dtype=None, complex_ok=False, copy=False):
    """
    Validate an input array.

    Parameters
    ----------
    x : array-like
        Input array to check.
    allow_nan : bool, default=True
        If False, raise error if array contains NaNs.
    allow_inf : bool, default=False
        If False, raise error if array contains infinities.
    dtype : data-type, optional
        If provided, convert array to this dtype.
    complex_ok : bool, default=False
        If False, raise error if array is complex.
    copy : bool, default=False
        Force a copy of the array.

    Returns
    -------
    x_checked : backend array
        Validated array, converted to correct backend and dtype.
    """
    # Get backend
    if xp is None:
        xp = array_namespace(x)

    x = _asarray(x, xp, dtype=dtype, copy=copy)

    # Check complex
    if not complex_ok:
        # Many backends have iscomplex
        is_complex = hasattr(xp, "iscomplex") and xp.any(xp.iscomplex(x))
        # fallback: imag != 0
        if not hasattr(xp, "iscomplex"):
            is_complex = xp.any(xp.not_equal(xp.imag(x), 0))
        if is_complex:
            raise ValueError("Complex values not allowed.")

    # Check NaNs
    if not allow_nan:
        if xp.any(xp.isnan(x)):
            raise ValueError("NaN values are not allowed.")

    # Check infinities
    if not allow_inf:
        if xp.any(xp.isinf(x)):
            raise ValueError("Infinity values are not allowed.")

    return x

