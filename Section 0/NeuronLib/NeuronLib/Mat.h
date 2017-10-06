/*
*
* Author: Yotam Salmon
* Date: 06/10/2017
*
*/
#pragma once
#include <functional>

/*
Represents a 2d matrix
*/
class Mat
{
public:
	Mat();
	Mat(int height, int width);
	Mat(int height, int width, float *data);
	Mat(const Mat& ref);
	~Mat();

	/*
	Returns the height (1st dimension) of the matrix
	*/
	int height();

	/*
	Returns the width (2nd dimension) of the matrix
	*/
	int width();


	/*
	Visualizes the matrix into std::cout
	*/
	void visualize();


	/*
	Random access to a specific matrix element at (row, col)
	*/
	float& operator()(int row, int col) const;

	/*
	Copy-assignment operator
	*/
	Mat& operator=(const Mat& ref);

	/*
	Checks if 2 matrices are equal (returns true if every (i,j) in ([0,h], [0,w]) satisfy ref[i,j] == this[i,j]
	*/
	bool operator==(const Mat& ref);

	/*
	Matrix addition
	*/
	Mat operator+(const Mat& ref);

	/*
	Matrix addition by scalar
	*/
	Mat operator+(float f);

	/*
	Matrix substraction
	*/
	Mat operator-(const Mat& ref);

	/*
	Matrix substraction by scalar
	*/
	Mat operator-(float f);

	/*
	Matrix multiplication by scalar
	*/
	Mat operator*(float f);

	/*
	Matrix division by scalar
	*/
	Mat operator/(float f);

	/*
	Matrix multiplication (dot product)
	*/
	Mat operator*(Mat& ref);

	/*
	Negates the matrix (-mat)
	*/
	static Mat neg(Mat& mat);

	/*
	Inverts the matrix (1/mat)
	*/
	static Mat inv(Mat& mat);


	/*
	Mask functions for operations that are not well-defined above
	For every (i,j) in ([0,h], [0,w]) in mat, runs the predicate with (mat[i,j], i, j) 
		and sets result[i,j] to the result from the predicate.
	*/
	static Mat mask(const Mat& mat, const std::function<float(float, int, int)>& pred);
	static Mat mask(const Mat& mat, const std::function<float(float)>& pred);

private:
	// The dimensions of the matrix
	int h = 0, w = 0;

	// The data of the matrix
	float* vals = nullptr;

	/*
	Throws an exception if shape(ref) != shape(this)
	*/
	void validate_same_size(const Mat& ref);
};

/*
Matrix addition by scalar (scalar first)
*/
Mat operator+(float scalar, Mat& mat);

/*
Negated matrix addition by scalar (scalar first)
*/
Mat operator-(float scalar, Mat& mat);

/*
Matrix multiplication by scalar (scalar first)
*/
Mat operator*(float scalar, Mat& mat);

/*
Inversed matrix multiplication by scalar (scalar first)
*/
Mat operator/(float scalar, Mat& mat);