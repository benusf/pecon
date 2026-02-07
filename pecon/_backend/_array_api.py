import numpy as np

from ._array_api_override import array_namespace

def _asarray(x, 
             xp=None, 
             dtype=None, 
             copy=False
            ):
    """
    Convert input to an array in the correct backend namespace.

    Parameters
    ----------
    x : array-like
        Input data.
    xp : module, optional
        The target namespace. If None, detected automatically.
    dtype : dtype, optional
        Desired data type.
    copy : bool, default=False
        Force copy of data.

    Returns
    -------
    array : backend array
    """
    if xp is None:
        xp = np
    if xp.__name__ == "numpy":
        x = np.asarray(x, dtype=dtype)
        if copy:
            x = x.copy()
        return x


    return xp.asarray(x, dtype=dtype, copy=copy)
