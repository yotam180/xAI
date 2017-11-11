#ifndef MAT
#define MAT

typedef struct mat {
	int h, w;
	double *vals;
} mat;

mat *zero_mat(int h, int w);
mat *new_mat(int h, int w, double *data);
mat *clone_mat(mat *ref);

#endif