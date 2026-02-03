cdef extern from "pecon_api.h":

    cdef struct Simple_OLS_Res:
        double alpha
        double beta
        double r
        double p

    Simple_OLS_Res SimpleOLS(double *x, double *y, int n)
