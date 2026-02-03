import numpy as np
from array import array


cpdef tuple double_view(object x):
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


cpdef _OLS(x, y, onedim):
    cdef:
        double[:] mvx
        double[:] mvy
        object owner
        int n

    owner, mvx = double_view(x)
    owner, mvy = double_view(y)

    nx = mvx.shape[0]

    cdef Simple_OLS_Res res

    if onedim:
        res = SimpleOLS(&mvx[0], &mvy[0], nx)
    else:
        pass


    return res.alpha, res.beta, res.r, res.p
