#pragma once
#include <math.h>
#include "Mat.h"

namespace np
{
	/*
	To perform exponent e^x for a matrix (or vector)
	*/
	Mat _exp(const Mat &ref)
	{
		return Mat::mask(ref, [](double v) -> double {
			return expf(v);
		});
	}

	/*
	To compute the sigmoid value of z
	*/
	double sigmoid(double z)
	{
		return 1 / (1 + expf(z));
	}

	/*
	To compute the sigmoid value of matrix z
	*/
	Mat sigmoid(const Mat& z)
	{
		return 1 / (1 + _exp(z)); // I would not lie. I really love myself for this line of code.
	}

	/*
	To compute the prime sigmoid value of matrix z
	*/
	Mat sigmoid_prime(const Mat& z)
	{
		return np::sigmoid(z).hadamard(1 - np::sigmoid(z));
	}
}