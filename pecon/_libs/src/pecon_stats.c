#include "pecon_api.h"
#include <math.h>

double pecon_mean(const double *x, int n) {
    return 1;
}
Corr_Res pecon_corr(double *x, double *y, int n) {
  Corr_Res res;
  double sum_x = 0, sum_y = 0;
  double sum_x2 = 0, sum_y2 = 0, sum_xy = 0;

  for (int i = 0; i < n; ++i) {
    sum_x += x[i];
    sum_y += y[i];
  }

  double mean_x = sum_x / n;
  double mean_y = sum_y / n;

  for (int i = 0; i < n; ++i) {
    double dx = x[i] - mean_x;
    double dy = y[i] - mean_y;
    sum_xy += dx * dy;
    sum_x2 += dx * dx;
    sum_y2 += dy * dy;
  }

  res.coef = sum_xy / sqrt(sum_x2 * sum_y2);
  double rs = sqrt((1 - pow(res.coef, 2)) / (n - 2));
  res.pvalue = res.coef / rs;

  return res;
}
