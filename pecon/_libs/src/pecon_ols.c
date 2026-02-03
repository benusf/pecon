#include "pecon_api.h"

Simple_OLS_Res SimpleOLS(double *x, double *y, int n) {
  Simple_OLS_Res res;
  double num = 0.0;
  double den = 0.0;
  double meanx = pecon_mean(x, n);
  double meany = pecon_mean(y, n);

  for (int i = 0; i < n; ++i) {
    double dx = x[i] - meanx;
    num += dx * (y[i] - meany);
    den += dx * dx;
  }
  Corr_Res c_res;
  c_res = pecon_corr(x, y, n);

  res.beta = num / den;
  res.alpha = meany - res.beta * meanx;
  double r = c_res.coef * c_res.coef;
  res.r = r * r;
  res.p = c_res.pvalue;

  return res;
}
