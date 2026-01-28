cdef extern from "pecon_stats.h":

    cdef struct Corr_Res:
        double coef
        double pvalue

    Corr_Res pecon_corr(double *x, double *y, int n)

# cpdef tuple correlation(list x, list y)
