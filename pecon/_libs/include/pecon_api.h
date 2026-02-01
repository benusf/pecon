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
} Corr_Res;

/* =========================
   Statistics
   ========================= */
double pecon_mean(const double *x, int n);
double pecon_var(const double *x, int n);
double pecon_std(const double *x, int n);
double pecon_cov(double *x, double *y, int n);
Corr_Res pecon_corr(double *x, double *y, int n);

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
