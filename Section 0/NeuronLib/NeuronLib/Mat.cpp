/*
 * 
 * Author: Yotam Salmon
 * Date: 06/10/2017
 * 
 */

#include "Mat.h"
#include <iostream>

// File might need some cleanup

using namespace std;

/*
Constructs an empty matrix
*/
Mat::Mat()
{
	this->vals = nullptr;
	this->h = this->w = 0;
}

/*
Constructs a zero-filled matrix of dimensions height,width
*/
Mat::Mat(int height, int width)
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

/*
Constructs a matrix with dimensions of height,width and fills it with data
data is preferred to be a pointer-cast of a 2d array.
*/
Mat::Mat(int height, int width, float * data)
{
	this->h = height;
	this->w = width;
	this->vals = new float[h * w];
	for (int i = 0; i < h; i++)
	{
		for (int j = 0; j < w; j++)
		{
			(*this)(i, j) = *(data + i * w + j);
		}
	}
}

/*
Copy constructor
*/
Mat::Mat(const Mat & ref)
{
	this->h = ref.h;
	this->w = ref.w;
	this->vals = new float[h * w];
	for (int i = 0; i < h; i++)
	{
		for (int j = 0; j < w; j++)
		{
			(*this)(i, j) = ref(i, j);
		}
	}
}

/*
Destructor - deletes the matrix
*/
Mat::~Mat()
{
	delete[] vals;
	vals = nullptr;
}

/*
Returns the height of the matrix (1st dimension)
*/
int Mat::height()
{
	return h;
}

/*
Returns the width of the matrix (2nd dimension)
*/
int Mat::width()
{
	return w;
}

/*
Random access operator (row, col) to a matrix element.
Can be used to get and set.
*/
float & Mat::operator()(int row, int col) const
{
	return *(vals + row * w + col);
}

/*
Copy operator
*/
Mat & Mat::operator=(const Mat & ref)
{
	this->h = ref.h;
	this->w = ref.w;
	if (vals != nullptr)
		delete[] this->vals;
	this->vals = new float[h * w];

	for (int i = 0; i < h; i++)
	{
		for (int j = 0; j < w; j++)
		{
			(*this)(i, j) = ref(i, j);
		}
	}
	return *this;
}

/*
Compares two matrices. Returns true if for any i,j in matrix a, b[i, j] = a[i, j]
*/
bool Mat::operator==(const Mat & ref)
{
	for (int i = 0; i < h; i++)
	{
		for (int j = 0; j < w; j++)
		{
			if (ref(i, j) != (*this)(i, j)) 
			{
				return false;
			}
		}
	}
	return true;
}

/*
Adds two matrices and returns the result
*/
Mat Mat::operator+(const Mat & ref)
{
	validate_same_size(ref);
	return Mat::mask(ref, [this](float v, int row, int col) -> int {
		return (*this)(row, col) + v;
	});
}

/*
Adds a scalar to a matrix and returns the result.
*/
Mat Mat::operator+(float f)
{
	return Mat::mask(*this, [f](float v) -> int {
		return v + f;
	});
}

Mat Mat::operator-(const Mat & ref)
{
	validate_same_size(ref);
	return Mat::mask(ref, [this](float v, int row, int col) -> int {
		return (*this)(row, col) - v;
	});
}

Mat Mat::operator-(float f)
{
	return Mat::mask(*this, [f](float v) {
		return v - f;
	});
}

Mat Mat::operator*(float f)
{
	return Mat::mask(*this, [f](float v) {
		return v * f;
	});
}

Mat Mat::operator/(float f)
{
	return Mat::mask(*this, [f](float v) {
		return v / f;
	});
}

Mat Mat::neg(Mat & mat)
{
	return Mat::mask(mat, [](float v) {
		return -v;
	});
}

Mat Mat::inv(Mat & mat)
{
	return Mat::mask(mat, [](float v) {
		return 1/v;
	});
}

Mat Mat::mask(const Mat & matrix, const std::function<float(float, int, int)>& pred)
{
	Mat result(matrix.h, matrix.w);
	for (int i = 0; i < matrix.h; i++)
	{
		for (int j = 0; j < matrix.w; j++)
		{
			result(i, j) = pred(matrix(i, j), i, j);
		}
	}
	return result;
}

Mat Mat::mask(const Mat & matrix, const std::function<float(float)>& pred)
{
	Mat result(matrix.h, matrix.w);
	for (int i = 0; i < matrix.h; i++)
	{
		for (int j = 0; j < matrix.w; j++)
		{
			result(i, j) = pred(matrix(i, j));
		}
	}
	return result;
}

void Mat::validate_same_size(const Mat & ref)
{
	if (h != ref.h || w != ref.w)
	{
		throw "Matrices must be of the same size";
	}
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

Mat operator+(float scalar, Mat & mat)
{
	return Mat::mask(mat, [scalar](float v) {
		return scalar + v;
	});
}

Mat operator-(float scalar, Mat & mat)
{
	return Mat::mask(mat, [scalar](float v) {
		return scalar - v;
	});
}

Mat operator*(float scalar, Mat & mat)
{
	return Mat::mask(mat, [scalar](float v) {
		return scalar * v;
	});
}

Mat operator/(float scalar, Mat & mat)
{
	return Mat::mask(mat, [scalar](float v) {
		return scalar / v;
	});
}
