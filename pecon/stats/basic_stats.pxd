cdef extern from "pecon_api.h":

    double pecon_mean(const double *x, int n)
    double pecon_var(const double *x, int n, int ddof)
    double pecon_std(const double *x, int n, int ddof)
    double pecon_cov(double *x, double *y, int n, int ddof)

    cdef struct Corr_Res:
        double coef
        double pvalue
        double ts

    Corr_Res pecon_corr(double *x, double *y, int n)
