#include "pecon_api.h"
#include <math.h>

double pecon_mean(const double *x, int n) {
  double sum = 0, mean;

  for (int i = 0; i < n; ++i) {
    sum += x[i];
  }
  mean = sum / n;

  return mean;
}

double pecon_var(const double *x, int n) {
  double sum = 0, var, xx;
  double meanx = pecon_mean(x, n);

  for (int i = 0; i < n; ++i) {
    xx = pow((x[i] - meanx), 2);
    sum += xx;
  }
  var = sum / (n - 1);

  return var;
}

double pecon_std(const double *x, int n) {
  double var = pecon_var(x, n);
  double std = sqrt(var);

  return std;
}

double pecon_cov(double *x, double *y, int n) {
  double sum = 0, cov, dxy;
  double meanx = pecon_mean(x, n);
  double meany = pecon_mean(y, n);

  for (int i = 0; i < n; ++i) {
    dxy = (x[i] * y[i] - meanx * meany);
    sum += dxy;
  }
  cov = sum / n;

  return cov;
}

Corr_Res pecon_corr(double *x, double *y, int n) {
  Corr_Res res;
  double sum_x2 = 0, sum_y2 = 0, sum_xy = 0;

  double mean_x = pecon_mean(x, n);
  double mean_y = pecon_mean(y, n);

  for (int i = 0; i < n; ++i) {
    double dx = x[i] - mean_x;
    double dy = y[i] - mean_y;
    sum_xy += dx * dy;
    sum_x2 += dx * dx;
    sum_y2 += dy * dy;
  }

  res.coef = sum_xy / sqrt(sum_x2 * sum_y2);
  double rs = sqrt((1 - pow(res.coef, 2)) / (n - 2));

  if (rs) {
    res.pvalue = res.coef / rs;
  } else {
    res.pvalue = 0.0;
  }

  return res;
}
