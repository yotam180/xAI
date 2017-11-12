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

double *el(mat *ref, int row, int col);

#endif