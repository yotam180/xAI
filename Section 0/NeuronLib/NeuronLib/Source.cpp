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
	n.save("network1.net");
	n.getLayerWeights(0).visualize();

	Network m("network1.net");
	m.getLayerWeights(0).visualize();

	system("pause");
	return 0;
}