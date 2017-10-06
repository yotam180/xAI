#include <iostream>

#include "Mat.h"
using namespace std;

int main(void)
{
	// Just testing out basic matrices operations

	float dat[][4] = {
		{ 1, 2, 3, 4 },
		{ 2, 3, 6, 7 },
		{ 1, 2, 2, 2 }
	};
	float dat2[][4] = {
		{2, 3, 3, 3},
		{1, 9, 9, 2},
		{0, 0, 1, 1},
	};
	Mat a(3, 4, (float*)dat);
	Mat b(3, 4, (float*)dat2);
	Mat c = 5 / a;
	c.visualize();
	system("pause");
	return 0;
}