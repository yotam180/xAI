#pragma once


namespace np
{
	/*
	Adding 2 matrices
	a - first matrix
	b - second matrix
	dim1, dim2 - dimensions of the matrices (must be the same)
	out - output matrix
	*/
	void add(float* a, float* b, int dim1, int dim2, float* out)
	{
		for (int i = 0; i < dim1; i++)
		{
			for (int j = 0; j < dim2; j++)
			{
				*(out + dim2 * i + j) = *(a + dim2 * i + j) + *(b + dim2 * i + j);
			}
		}
	}
	/*
	Multiplying 2 matrices
	a - first matrix
	b - second matrix
	dim1a, dim2a - dimensions of matrix a
	dim1b, dim2b - dimensions of matrix b
	out - output matrix
	*/
	void mul(float* a, float* b, int dim1a, int dim2a, int dim1b, int dim2b, float* out)
	{
		if (dim1b != dim2a)
		{
			throw "First dimension of matrix b must be equal to second dimension of matrix a";
		}
		for (int i = 0; i < dim1a; i++)
		{
			for (int j = 0; j < dim2b; j++)
			{
				float sum = 0;
				for (int k = 0; k < dim2a; k++)
				{
					sum += *(a + k * dim2a + j) * *(w + k)
				}
			}
		}
	}
}