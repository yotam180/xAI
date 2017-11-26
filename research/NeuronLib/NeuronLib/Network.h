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
	void train(const vector<Vec*>& x, const vector<Vec*>& y, int epochs, int mini_batch_size, double learning_rate, const vector<Vec*>& tx = vector<Vec*>(), const function<bool(int, Vec&)>& pred = [](int a, Vec& b) -> bool {});


	void save(string file_name); // To save to file

	Network& operator=(const Network& ref);

	// Temporarily here - put back!
	tuple<Vec*, Mat*> backprop(Vec& x, Vec& y);
	void update_mini_batch(vector<Vec*> x, vector<Vec*> y, double learning_rate);


private:
	int layers;
	int *sizes;

	Vec *biases;
	Mat *weights;

	double evaluate(vector<Vec*> x, const function<bool(int, Vec&)>& pred);
	Vec cost_derivative(Vec activations, Vec y);
};

