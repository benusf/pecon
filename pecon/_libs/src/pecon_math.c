#include "pecon_api.h"
#include <stdio.h>
#include <stdlib.h>

Matrix create_mat(int rows, int cols) {
  Matrix m;
  m.rows = rows;
  m.cols = cols;
  m.data = (double **)malloc(rows * sizeof(double *));
  for (int i = 0; i < rows; ++i) {
    m.data[i] = (double *)malloc(cols * sizeof(double));
    for (int j = 0; j < cols; ++j) {
      m.data[i][j] = 0.0;
    }
  }

  return m;
}

void free_mat(Matrix m) {
  for (int i = 0; i < m.rows; ++i) {
    free(m.data[i]);
  }
  free(m.data);
}

Matrix transpose_mat(Matrix m) {

  Matrix result = create_mat(m.cols, m.rows);
  for (int i = 0; i < m.rows; ++i) {
    for (int j = 0; i < m.cols; ++j) {
      result.data[j][i] = result.data[i][j];
    }
  }

  return result;
}

Matrix multi_mat(Matrix a, Matrix b) {
  Matrix result = create_mat(a.cols, b.rows);
  if (a.cols != b.rows) {
    printf("error");
  } else {
    for (int i = 0; i < a.rows; ++i) {
      for (int j = 0; j < b.cols; ++j) {
        double sum = 0.0;
        for (int k = 0; k < a.cols; ++k) {
          sum += a.data[i][k] * b.data[k][j];
        }

        result.data[i][j] = sum;
      }
    }
  }

  return result;
}
