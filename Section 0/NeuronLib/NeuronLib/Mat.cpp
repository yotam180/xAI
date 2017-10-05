#include "Mat.h"
#include <iostream>

using namespace std;

/*

Fuck my life, I'll have to rewrite this shit tommorow.
This is full of bugs and will be a weak mainstay for the project.
Please, drunk self, remember to fix this crap before you move on 
to more complex stuff.

Yotam.

*/
Mat::Mat()
{
	this->vals = nullptr;
	this->h = this->w = 0;
}

Mat::Mat(int width, int height)
{
	this->vals = new float[height * width];
	this->h = height;
	this->w = width;
	for (int i = 0; i < h; i++)
	{
		for (int j = 0; j < w; j++)
		{
			(*this)(i, j) = 0;
		}
	}
}

Mat::Mat(const Mat & ref)
{
	this->h = ref.h;
	this->w = ref.w;
	this->vals = new float[h * w];
	for (int i = 0; i < w; i++)
	{
		for (int j = 0; j < h; j++)
		{
			(*this)(i, j) = ref(i, j);
		}
	}
}


Mat::~Mat()
{
	delete[] vals;
}

int Mat::height()
{
	return h;
}

int Mat::width()
{
	return w;
}

float & Mat::operator()(int x, int y) const
{
	return *(vals + y * w + x);
}

Mat & Mat::operator=(const Mat & ref)
{
	this->h = ref.h;
	this->w = ref.w;
	delete[] this->vals;
	this->vals = new float[h * w];
	for (int i = 0; i < w; i++)
	{
		for (int j = 0; j < h; j++)
		{
			(*this)(i, j) = ref(i, j);
		}
	}
	return *this;
}

void Mat::visualize()
{
	cout << "[";
	for (int i = 0; i < h; i++)
	{
		if (i != 0)
			cout << ", " << endl << " ";
		cout << "[";
		for (int j = 0; j < w; j++)
		{
			if (j != 0)
				cout << ", ";
			cout << (*this)(i, j);
		}
		cout << "]";
	}
	cout << "]" << endl;
}
