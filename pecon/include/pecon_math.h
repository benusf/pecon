#ifndef PECON_MATH_H
#define PECON_MATH_H

typedef struct {
  double **data;
  int rows;
  int cols;
} Matrix;

Matrix create_mat(int rows, int cols);
void free_mat(Matrix m);
Matrix transpose_mat(Matrix m);
Matrix multi_mat(Matrix a, Matrix b);

#endif // !PECON_MATH
