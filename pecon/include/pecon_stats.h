#ifndef PECON_CORR_H
#define PECON_CORR_H

typedef struct Corr_Res {
  double coef;
  double pvalue;
} Corr_Res;

Corr_Res pecon_corr(double *x, double *y, int n);

#endif
