#include <iostream>

#include "Mat.h"
using namespace std;

int main(void)
{
	// Just testing out basic matrices operations

	float dat1[][3] = {
		{ 1, 2, 3 },
		{ 4, 5, 6 }
	};
	float dat2[][2] = {
		{ 7,  8  },
		{ 9,  10 },
		{ 11, 12 }
	};
	Mat m1(2, 3, (float*)dat1);
	Mat m2(3, 2, (float*)dat2);
	Mat mul = m2 * m1;
	mul.visualize();
	system("pause");
	return 0;
}