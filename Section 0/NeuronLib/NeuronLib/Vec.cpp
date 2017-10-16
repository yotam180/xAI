#pragma once
#ifdef UNIT_TEST
#include "stdafx.h"
#endif

#include "Vec.h"

Vec::Vec(int dim, const function<double(int)>& pred)
{
	h = dim;
	w = 1;
	vals = new double[h];
	for (int i = 0; i < h; i++)
	{
		(*this)(i) = pred(i);
	}
}

Vec::~Vec()
{
}

double & Vec::operator()(int row) const
{
	return *(vals + row);
}

int Vec::length()
{
	return h;
}
