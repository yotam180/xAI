#pragma once
#include <iostream>
#include <cstdlib>
#include <vector>

#include "Vec.h"

using namespace std;

class Network
{
public:
	Network();
	Network(int layers, int *sizes);
	Network(const Network& ref);
	Network(string file_name); // To load a saved network from file
	~Network();

	int getDepth();
	int getLayerSize(int layer);
	Vec getLayerBiases(int layer);
	Mat getLayerWeights(int layer);

	Vec feed_forward(Vec& x);

	void save(string file_name); // To save to file

	Network& operator=(const Network& ref);

private:
	int layers;
	int *sizes;

	Vec *biases;
	Mat *weights;
};

