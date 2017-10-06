#pragma once
#include <math.h>
#include "Mat.h"

namespace np
{
	/*
	To perform exponent e^x
	*/
	float exp(float z)
	{
		return exp(z);
	}

	/*
	To perform exponent e^x for a matrix (or vector)
	*/
	Mat exp(Mat &ref)
	{
		return Mat::mask(ref, [](float v) -> int {
			return exp(v);
		});
	}
}