from array import array
import numpy as np


cdef inline tuple as_double_view(object x):
    cdef double[:] mv

    # --- NumPy arrays ---
    if hasattr(x, "__array__"):
        arr = np.asarray(x, dtype=np.float64)
        if not arr.flags["C_CONTIGUOUS"]:
            arr = np.ascontiguousarray(arr)
        mv = arr
        return arr, mv

    # --- buffer protocol (array.array, memoryview) ---
    try:
        mv = x  # try typed memoryview
        return x, mv
    except Exception:
        pass

    # --- Python sequences ---
    if isinstance(x, (list, tuple)):
        arr = array("d", x)
        mv = arr
        return arr, mv

    raise TypeError("Expected array-like object (list, array, buffer, ndarray)")


cpdef _mean(object x):
    cdef:
        double[:] mv
        object owner
        int n

    owner, mv = as_double_view(x)
    n = mv.shape[0]

    if n == 0:
        msg = "empty input"
        raise ValueError(msg)

    res = pecon_mean(&mv[0], n)
    return res

cpdef _var(x):
    cdef:
        double[:] mv
        object owner
        int n

    owner, mv = as_double_view(x)
    n = mv.shape[0]

    if n == 0:
        msg = "empty input"
        raise ValueError(msg)
    if n < 2:
        msg = "array must contain at least two values"
        raise ValueError(msg)

    res = pecon_var(&mv[0], n)
    return res

cpdef _std(x):
    cdef:
        double[:] mv
        object owner
        int n

    owner, mv = as_double_view(x)
    n = mv.shape[0]

    if n == 0:
        msg = "empty input"
        raise ValueError(msg)
    if n < 2:
        msg = "array must contain at least two values"
        raise ValueError(msg)

    res = pecon_std(&mv[0], n)
    return res

cpdef _cov(x, y):
    cdef:
        double[:] mvx
        double[:] mvy
        object owner
        int n

    owner, mvx = as_double_view(x)
    owner, mvy = as_double_view(y)

    nx = mvx.shape[0]
    ny = mvy.shape[0]

    if nx == 0:
        msg = "empty input"
        raise ValueError(msg)
    if nx == 1:
        msg = "array must contain at least two values"
        raise ValueError(msg)
    if nx != ny:
        msg = "x and y must have same lenght"
        raise ValueError(msg)

    res = pecon_cov(&mvx[0], &mvy[0], nx)

    return res

cpdef tuple _corr(x, y):
    cdef:
        double[:] mvx
        double[:] mvy
        object owner
        int n

    owner, mvx = as_double_view(x)
    owner, mvy = as_double_view(x)

    nx = mvx.shape[0]
    ny = mvy.shape[0]

    if nx != ny:
        msg = "x and y must have same lenght"
        raise ValueError(msg)

    cdef Corr_Res res
    res = pecon_corr(&mvx[0], &mvy[0], nx)

    return res.coef, res.pvalue
