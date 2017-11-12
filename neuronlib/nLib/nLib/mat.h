#ifndef MAT
#define MAT

#ifndef TRUE
#define TRUE 1
#endif

#ifndef FALSE
#define FALSE 0
#endif

typedef struct mat {
	int h, w;
	double *data;
} mat;

mat *zero_mat(int h, int w);
mat *alloc_mat(int h, int w);
mat *new_mat(int h, int w, double *data);
mat *clone_mat(mat *ref);

void visualize_mat(mat *ref);
void visualize_int_mat(mat *ref);

int add_mat(mat *a, mat *b, mat *ref);
int sub_mat(mat *a, mat *b, mat *ref);
int add_scal(mat *a, double b, mat *ref);
int sub_scal(mat *a, double b, mat *ref);
int mul_scal(mat *a, double b, mat *ref);
int div_scal(mat *a, double b, mat *ref);
int div_mat_scal(double a, mat *b, mat *ref);
int mul_mat(mat *a, mat *b, mat *ref);

double *el(mat *ref, int row, int col);

#endif