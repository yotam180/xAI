#pragma once
#ifndef binfile
#define binfile a
#include <iostream>
#include <fstream>
#include <ostream>
#include <istream>

using namespace std;

typedef char byte;

#define DOUBLE_SIZE 8 // In bytes

namespace bin
{
	double readdouble(fstream& file)
	{
		byte n[DOUBLE_SIZE];
		file.read(n, DOUBLE_SIZE);
		double *f = reinterpret_cast<double*>(n);
		return *f;
	}

	int readInt(fstream& file)
	{
		byte n[DOUBLE_SIZE];
		file.read(n, DOUBLE_SIZE);
		int *f = reinterpret_cast<int*>(n);
		return *f;
	}

	void writedouble(fstream& file, double f)
	{
		byte *n = reinterpret_cast<byte*>(&f);
		file.write(n, DOUBLE_SIZE);
	}

	void writeInt(fstream& file, int f)
	{
		byte *n = reinterpret_cast<byte*>(&f);
		file.write(n, DOUBLE_SIZE);
	}
}

#endif