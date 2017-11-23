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
	
	int sizes[] = { 1, 15, 10, 1 };
	Network n(4, sizes);
	vector<Vec*> xs;
	vector<Vec*> ys;
	vector<Vec*> tx;
	vector<Vec*> ty;
	double x;
	double y;
	for (int i = 0; i < 100; i++) {
		x = 0.01 * i;// (double)rand() / RAND_MAX;
		y = x > 0.3 && x < 0.6 ? 1 : 0;
		xs.push_back(new Vec(1, &x));
		ys.push_back(new Vec(1, &y));
	}
	for (int i = 0; i < 100; i++) {
		x = 0.01 * i;// (double)rand() / RAND_MAX;
		y = x > 0.3 && x < 0.6 ? 1 : 0;
		tx.push_back(new Vec(1, &x));
		ty.push_back(new Vec(1, &y));
	}

	n.train(xs, ys, 30, 100, 0.15, tx, [ty](int i, Vec& y) -> bool {
		return round(y(0)) == round((*ty[i])(0));
	});

	for (int i = 0; i < 100; i++) {
		delete xs[i];
		delete ys[i];
	}
	for (int i = 0; i < 100; i++) {
		delete tx[i];
		delete ty[i];
	}

	//double input;
	//cin >> input;
	//Vec m(1, &input);
	//Vec res = n.feed_forward(m);
	
	/*double in = 0.4;
	double out = 1;
	Vec vin(1, &in);
	Vec vout(1, &out);

	n.feed_forward(vin).visualize();

	tuple<Vec*, Mat*> delta = n.backprop(vin, vout);
	std::get<0>(delta)[0].visualize();*/


	//n.getLayerWeights(1).visualize();
	//n.getLayerBiases(1).visualize();

	system("pause");
	return 0;
}