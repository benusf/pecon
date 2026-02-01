cdef extern from "pecon_api.h":

    double pecon_mean(const double *x, int n)
    double pecon_var(const double *x, int n)
    double pecon_std(const double *x, int n)
    double pecon_cov(double *x, double *y, int n)

    cdef struct Corr_Res:
        double coef
        double pvalue

    Corr_Res pecon_corr(double *x, double *y, int n)
