#include "Vec.h"

Vec::Vec(int dim, const function<float(int)>& pred)
{
	h = dim;
	w = 1;
	vals = new float[h];
	for (int i = 0; i < h; i++)
	{
		(*this)(i) = pred(i);
	}
}

Vec::~Vec()
{
}

float & Vec::operator()(int row) const
{
	return *(vals + row);
}

int Vec::length()
{
	return h;
}
