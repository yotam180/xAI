#include <iostream>

#include "Mat.h"
using namespace std;

int main(void)
{
	Mat a(3, 4);
	a(0, 1) = 5;
	a(2, 2) = 4;
	//Mat b(a);
	//b(1, 0) = 3;
	a.visualize();
	//b.visualize();

	system("pause");
	return 0;
}