"""
_pecon._backend._array_api.py

Provides a SciPy-style Array API wrapper for pecon.

Supports NumPy, CuPy, Torch, JAX, Dask arrays.
Includes:
- array_namespace: returns correct backend for input arrays
- _asarray: converts input to backend array safely
- global switch to disable array API
"""

from pecon._external.array_api_compat import array_namespace as _array_namespace
import numpy as np

# Global switch: disable Array API, always use NumPy
PECON_ARRAY_API = True

def array_namespace(*arrays, strict=False):
    """
    Determine the appropriate array API namespace for the input arrays.

    Parameters
    ----------
    *arrays : array-like
        One or more arrays whose namespace is used to select the backend.
    strict : bool, default=False
        If True, raise an error when arrays from different namespaces are detected.

    Returns
    -------
    xp : module
        Array API-compatible module (numpy, cupy, torch, jax, dask).
    """
    if not PECON_ARRAY_API:
        return np


    arrays = tuple(a for a in arrays if a is not None)

    # If all inputs are Python scalars or lists, default to NumPy
    if all(isinstance(a, (list, int, float, complex)) for a in arrays):
        return np

    # Convert Python lists/scalars to NumPy arrays for backend detection
    arrays_fixed = [np.asarray(a) if isinstance(a, (list, int, float, complex)) else a
                    for a in arrays]


    xp = _array_namespace(*arrays)

    if strict:
        # Check all arrays belong to same namespace
        for a in arrays:
            if not is_same_namespace(a, xp):
                raise TypeError(
                    f"Arrays belong to different backends: {type(a)} vs {xp.__name__}"
                )

    return xp

def is_same_namespace(x, xp):
    """
    Check if array x belongs to the backend xp.

    Supports numpy, cupy, torch, jax, dask.
    """
    # NumPy
    if xp.__name__ == "numpy":
        import numpy as np
        return isinstance(x, np.ndarray)
    # CuPy
    if xp.__name__ == "cupy":
        import cupy as cp
        return isinstance(x, cp.ndarray)
    # Torch
    if xp.__name__ == "torch":
        import torch
        return isinstance(x, torch.Tensor)
    # JAX
    if xp.__name__ == "jax.numpy":
        import jax.numpy as jnp
        return isinstance(x, jnp.ndarray)
    # Dask
    if xp.__name__ == "dask.array":
        import dask.array as da
        return isinstance(x, da.Array)
    return False



default_xp = np  # fallback default

