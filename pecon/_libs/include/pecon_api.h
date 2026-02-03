#ifndef PECON_API_H
#define PECON_API_H


#ifdef __cplusplus
extern "C" {
#endif

/* =========================
   Versioning
   ========================= */
#define PECON_API_VERSION 1

/* =========================
   Common types
   ========================= */

typedef struct Corr_Res {
  double coef;
  double pvalue;
  double ts;
} Corr_Res;

typedef struct Simple_OLS_Res {
  double alpha;
  double beta;
  double r;
  double p;
} Simple_OLS_Res;

/* =========================
   Statistics
   ========================= */
double pecon_mean(const double *x, int n);
double pecon_var(const double *x, int n, int ddof);
double pecon_std(const double *x, int n, int ddof);
double pecon_cov(double *x, double *y, int n, int ddof);
static double betacf(double a, double b, double x);
static double betainc(double a, double b, double x);
Corr_Res pecon_corr(double *x, double *y, int n);
Simple_OLS_Res SimpleOLS(double *x, double *y, int n);

/* =========================
   OLS
   ========================= */
typedef struct {
  double **data;
  int rows;
  int cols;
} Matrix;

Matrix create_mat(int rows, int cols);
void free_mat(Matrix m);
Matrix transpose_mat(Matrix m);
Matrix multi_mat(Matrix a, Matrix b);

#ifdef __cplusplus
}
#endif

#endif /* PECON_API_H */
