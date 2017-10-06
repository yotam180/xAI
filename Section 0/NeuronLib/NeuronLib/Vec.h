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
	Vec(int dim, float* data) : Mat(dim, 1, data) {}
	Vec(int dim, const function<float(int)>& pred);
	Vec(const Vec& ref) : Mat(ref) {}
	~Vec();

	float& operator()(int row) const;

	static float dot(const Vec& a, const Vec& b); // TODO implement later (not necessary for now)
	static float cross(const Vec& a, const Vec& b);

	int length();
};

