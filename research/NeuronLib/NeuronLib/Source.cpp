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
	
	int sizes[] = { 5, 6, 3, 4 };
	Network n(4, sizes);
	double input[] = { 1, 0.5, 0, 0.3, 0.7 };
	double output[] = { 0, 1, 0, 0 };
	Vec x(5, (double*)input);
	Vec y(4, (double*)output);
	tuple<Vec*, Mat*> res = n.backprop(x, y);
	
	for (int i = 0; i < 3; i++)
	{
		std::get<0>(res)[i].visualize();
	}

	delete[] std::get<0>(res);
	delete[] std::get<1>(res);

	system("pause");
	return 0;
}