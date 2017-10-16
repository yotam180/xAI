#include <iostream>
#include <time.h>
#include <fstream>

#include "Mat.h"
#include "Vec.h"
#include "Network.h"
using namespace std;

int main(void)
{
	srand(time(NULL));
	double a[][3] = {
		{ 1, 2, 3 },
		{ 6, 4, 2.3 },
		{ 1, 9, 9 }
	};
	Mat ma(3, 3, (double*)a);
	double e[][3] = {
		{ 5, 10, 15 },
		{ 30, 20, 11.5 },
		{ 5, 45, 45 }
	};
	Mat me(3, 3, (double*)e);
	Mat mr = ma * 5;
	Mat mr2 = 5 * ma;
	Mat mr3 = ma / (1.0 / 5.0);
	mr3.visualize();

	system("pause");
	return 0;
}