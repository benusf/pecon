#include "pecon_api.h"
#include <math.h>
#include <float.h>

double pecon_mean(const double *x, int n) {
  double sum = 0, mean;

  for (int i = 0; i < n; ++i) {
    sum += x[i];
  }
  mean = sum / n;

  return mean;
}

double pecon_var(const double *x, int n, int ddof) {
  double sum = 0, var, xx;
  double meanx = pecon_mean(x, n);

  for (int i = 0; i < n; ++i) {
    xx = pow((x[i] - meanx), 2);
    sum += xx;
  }

  var = sum / (n - ddof);

  return var;
}

double pecon_std(const double *x, int n, int ddof) {
  double var = pecon_var(x, n, ddof);
  double std = sqrt(var);

  return std;
}

double pecon_cov(double *x, double *y, int n, int ddof) {
  double sum = 0, cov, dxy;
  double meanx = pecon_mean(x, n);
  double meany = pecon_mean(y, n);

  for (int i = 0; i < n; ++i) {
    dxy = (x[i] * y[i] - meanx * meany);
    sum += dxy;
  }

  cov = sum / (n - ddof);

  return cov;
}


static double betacf(double a, double b, double x) {
  const int MAXIT = 100;
  const double EPS = 3.0e-7;
  const double FPMIN = 1.0e-30;

  double qab = a + b;
  double qap = a + 1.0;
  double qam = a - 1.0;
  double c = 1.0;
  double d = 1.0 - qab * x / qap;
  if (fabs(d) < FPMIN)
    d = FPMIN;
  d = 1.0 / d;
  double h = d;

  for (int m = 1; m <= MAXIT; m++) {
    int m2 = 2 * m;
    double aa = m * (b - m) * x / ((qam + m2) * (a + m2));
    d = 1.0 + aa * d;
    if (fabs(d) < FPMIN)
      d = FPMIN;
    c = 1.0 + aa / c;
    if (fabs(c) < FPMIN)
      c = FPMIN;
    d = 1.0 / d;
    h *= d * c;

    aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2));
    d = 1.0 + aa * d;
    if (fabs(d) < FPMIN)
      d = FPMIN;
    c = 1.0 + aa / c;
    if (fabs(c) < FPMIN)
      c = FPMIN;
    d = 1.0 / d;
    double del = d * c;
    h *= del;

    if (fabs(del - 1.0) < EPS)
      break;
  }
  return h;
}

static double betainc(double a, double b, double x) {
  if (x <= 0.0)
    return 0.0;
  if (x >= 1.0)
    return 1.0;

  double bt = exp(lgamma(a + b) - lgamma(a) - lgamma(b) + a * log(x) +
                  b * log(1.0 - x));

  if (x < (a + 1.0) / (a + b + 2.0))
    return bt * betacf(a, b, x) / a;
  else
    return 1.0 - bt * betacf(b, a, 1.0 - x) / b;
}

Corr_Res pecon_corr(double *x, double *y, int n) {
  Corr_Res res;
  res.coef = NAN;
  res.pvalue = NAN;
  res.ts = NAN;

  if (n < 3)
    return res;

  double mean_x = pecon_mean(x, n);
  double mean_y = pecon_mean(y, n);

  double sum_x2 = 0.0;
  double sum_y2 = 0.0;
  double sum_xy = 0.0;

  for (int i = 0; i < n; ++i) {
    double dx = x[i] - mean_x;
    double dy = y[i] - mean_y;
    sum_x2 += dx * dx;
    sum_y2 += dy * dy;
    sum_xy += dx * dy;
  }

  double denom = sqrt(sum_x2 * sum_y2);
  if (denom <= DBL_EPSILON)
    return res; // zero variance

  double r = sum_xy / denom;
  double t = r * sqrt((n - 2) / (1 - r * r));
  res.coef = r;
  res.ts = t;
  /* Guard numerical overflow */
  if (fabs(r) >= 1.0) {
    res.pvalue = 0.0;
    return res;
  }

  /* Exact Pearson p-value */
  double df = n - 2.0;
  double xval = 1.0 - r * r;

  res.pvalue = betainc(0.5 * df, 0.5, xval);

  return res;
}
