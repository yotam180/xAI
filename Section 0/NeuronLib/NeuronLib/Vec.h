#pragma once
#include "Mat.h"
#include <functional>

using namespace std;

class Vec:
	public Mat
{
public:
	Vec() : Mat() {}
	Vec(int dim) : Mat(dim, 1) {}
	Vec(int dim, double* data) : Mat(dim, 1, data) {}
	Vec(int dim, const function<double(int)>& pred);
	Vec(const Vec& ref) : Mat(ref) {}
	Vec(const Mat& ref) : Mat(ref.height(), 1)
	{
		for (int i = 0; i < h; i++)
		{
			(*this)(i) = ref(i, 0);
		}
	}
	~Vec();

	double& operator()(int row) const;

	static double dot(const Vec& a, const Vec& b); // TODO implement later (not necessary for now)
	static double cross(const Vec& a, const Vec& b);

	int length();
};

