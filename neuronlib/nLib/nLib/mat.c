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
}

void visualize_int_mat(mat * ref)
{
}

/*
Random access to a matrix element (by reference)
*/
double * el(mat * ref, int row, int col)
{
	return ref->data + row * ref->w + col;
}
