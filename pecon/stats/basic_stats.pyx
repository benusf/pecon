from array import array


cpdef tuple correlation(list x, list y):
    cdef int n = len(x)
    if len(y) != n:
        raise ValueError("x and y must have same lenght")

    cx = array('d', x)
    cy = array('d', y)

    cdef double[:] vx = cx
    cdef double[:] vy = cy

    cdef Corr_Res res
    res = pecon_corr(&vx[0], &vy[0], n)

    return res.coef, res.pvalue
