#pragma once
#ifndef binfile
#define binfile a
#include <iostream>
#include <fstream>
#include <ostream>
#include <istream>

using namespace std;

typedef char byte;

namespace bin
{
	float readFloat(fstream& file)
	{
		byte n[4];
		file.read(n, 4);
		float *f = reinterpret_cast<float*>(n);
		return *f;
	}

	int readInt(fstream& file)
	{
		byte n[4];
		file.read(n, 4);
		int *f = reinterpret_cast<int*>(n);
		return *f;
	}

	void writeFloat(fstream& file, float f)
	{
		byte *n = reinterpret_cast<byte*>(&f);
		file.write(n, 4);
	}

	void writeInt(fstream& file, int f)
	{
		byte *n = reinterpret_cast<byte*>(&f);
		file.write(n, 4);
	}
}

#endif