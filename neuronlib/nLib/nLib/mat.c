#include <stdio.h>

#include "mat.h"

/*
Initializes a matrix with zero values
*/
mat * zero_mat(int h, int w)
{
	// Allocating a matrix
	mat *m = (mat*)malloc(sizeof(mat));

	// Failsafe allocation
	if (m == NULL)
		return NULL;

	m->h = h;
	m->w = w;

	// Allocating data buffer
	m->data = (double*)calloc(h * w, sizeof(double));

	// Failsafe allocation
	if (m->data == NULL)
	{
		free(m);
		return NULL;
	}

	return m;
}

/*
Allocates a new matrix without initializing it
*/
mat * alloc_mat(int h, int w)
{
	// Allocating the matrix
	mat *m = (mat*)malloc(sizeof(mat));

	// Failsafe allocation
	if (m == NULL)
		return NULL;
	
	m->h = h;
	m->w = w;

	// Allocating data buffer
	m->data = (double*)malloc(h * w * sizeof(double));

	// Failsafe allocation
	if (m->data == NULL)
	{
		free(m);
		return NULL;
	}

	return m;
}

/*
Initializes a new matrix with preloaded data
*/
mat * new_mat(int h, int w, double * data)
{
	// Allocating a new matrix
	mat *m = alloc_mat(h, w);
	
	// Failsafe allocation
	if (m == NULL)
		return NULL;

	memcpy(m->data, data, h * w * sizeof(double));

	return m;
}

/*
Copies a matrix and returns a new one with the same values
*/
mat * clone_mat(mat * ref)
{
	return new_mat(ref->h, ref->w, ref->data);
}

void visualize_mat(mat * ref)
{
	printf("[");
	for (int i = 0; i < ref->h; i++)
	{
		if (i != 0)
			printf(", \n ");
		printf("[");

		for (int j = 0; j < ref->w; j++)
		{
			if (j != 0)
				printf(", ");

			printf("%.5f", *el(ref, i, j));
		}
		printf("]");
	}
	printf("]\n");
}

void visualize_int_mat(mat * ref)
{
	printf("[");
	for (int i = 0; i < ref->h; i++)
	{
		if (i != 0)
			printf(", \n ");
		printf("[");

		for (int j = 0; j < ref->w; j++)
		{
			if (j != 0)
				printf(", ");

			printf("%.0f", *el(ref, i, j));
		}
		printf("]");
	}
	printf("]\n");
}

int add_mat(mat * a, mat * b, mat * ref)
{
	if (a->h != b->h || a->w != b->w || a->h != ref->h || a->w != ref->w)
	{
		return FALSE;
	}
	for (int i = 0; i < a->h; i++)
	{
		for (int j = 0; j < a->w; j++)
		{
			*el(ref, i, j) = *el(a, i, j) + *el(b, i, j);
		}
	}
	return TRUE;
}

int sub_mat(mat * a, mat * b, mat * ref)
{
	mul_scal(b, -1, ref);
	return add_mat(a, ref, ref);
}

int add_scal(mat * a, double b, mat * ref)
{
	if (a->h != ref->h || a->w != ref->w)
	{
		return FALSE;
	}
	for (int i = 0; i < a->h; i++)
	{
		for (int j = 0; j < a->w; j++)
		{
			*el(ref, i, j) = *el(a, i, j) + b;
		}
	}
	return TRUE;
}

int sub_scal(mat * a, double b, mat * ref)
{
	return add_scal(a, -b, ref);
}

int mul_scal(mat * a, double b, mat * ref)
{
	if (a->h != ref->h || a->w != ref->w)
	{
		return FALSE;
	}
	for (int i = 0; i < a->h; i++)
	{
		for (int j = 0; j < a->w; j++)
		{
			*el(ref, i, j) = *el(a, i, j) * b;
		}
	}
	return TRUE;
}

int div_scal(mat * a, double b, mat * ref)
{
	return mul_scal(a, 1.0 / b, ref);
}

int div_mat_scal(double a, mat * b, mat * ref)
{
	if (b->h != ref->h || b->w != ref->w)
	{
		return FALSE;
	}
	for (int i = 0; i < b->h; i++)
	{
		for (int j = 0; j < b->w; j++)
		{
			*el(ref, i, j) = a / *el(b, i, j);
		}
	}
	return TRUE;
}

int mul_mat(mat * a, mat * b, mat *ref)
{
	if (a->w != b->h || ref->h != a->h || ref->w != b->w)
	{
		return FALSE;
	}
	for (int i = 0; i < a->h; i++)
	{
		for (int j = 0; j < b->w; j++)
		{
			double sum = 0;
			for (int k = 0; k < a->w; k++)
			{
				sum += *el(a, i, k) * *el(b, k, j);
			}
			*el(ref, i, j) = sum;
		}
	}
}

/*
Random access to a matrix element (by reference)
*/
double * el(mat * ref, int row, int col)
{
	return ref->data + row * ref->w + col;
}
