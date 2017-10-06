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
	int sizes[] = { 5, 3, 4 };
	Network n(3, sizes);
	double input[] = { 1, 0.5, 0, 0.3, 0.7 };
	Vec x(5, (double*)input);
	Vec y = n.feed_forward(x);
	y.visualize();

	system("pause");
	return 0;
}