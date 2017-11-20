#include "Network.h"
#include <fstream>
#include <random>
#include <algorithm>
#include <iterator>
#include <functional>

#include "binfile.h"
#include "np.h"
using namespace std;


Network::Network()
{
	sizes = nullptr;
	biases = nullptr;
	weights = nullptr;
}

Network::Network(int layers, int *sizes)
{
	// Setting network's base data
	this->layers = layers;
	this->sizes = new int[layers];
	for (int i = 0; i < layers; i++)
	{
		this->sizes[i] = *(sizes + i);
	}
	
	// Randomizing biases and weights
	biases = new Vec[layers - 1];
	for (int i = 0; i < layers - 1; i++)
	{
		biases[i] = Vec(sizes[i + 1]);
		for (int j = 0; j < sizes[i + 1]; j++)
		{
			biases[i](j) = (double)rand() / RAND_MAX;
		}
	}

	weights = new Mat[layers - 1];
	for (int i = 0; i < layers - 1; i++)
	{
		int l1 = sizes[i]; // Size of current layer
		int l2 = sizes[i + 1]; // Size of next layer
		weights[i] = Mat(l2, l1); //Notice that the matrix is constructed l2,l1 and not l1,l2 (why? *smirk*)

		for (int j = 0; j < l1; j++)
		{
			for (int k = 0; k < l2; k++)
			{
				weights[i](k, j) = (double)rand() / RAND_MAX;
			}
		}
	}
}

Network::Network(const Network & ref)
{
	// TODO make this one again (disappeared from the commit for a mysterious reason)
}

Network::Network(string file_name)
{
	fstream file;
	file.open(file_name, ios::in);
	int check = bin::readInt(file);
	if (check != 10)
	{
		throw string("Network file is not in the correct format");
	}
	layers = bin::readInt(file);
	sizes = new int[layers];
	for (int i = 0; i < layers; i++)
	{
		sizes[i] = bin::readInt(file);
	}
	check = bin::readInt(file);
	if (check != 11)
	{
		throw string("Network file is not in the correct format");
	}
	biases = new Vec[layers - 1];
	for (int i = 0; i < layers - 1; i++)
	{
		biases[i] = Vec(sizes[i + 1]);
		for (int j = 0; j < sizes[i + 1]; j++)
		{
			biases[i](j) = bin::readdouble(file);
		}
	}
	check = bin::readInt(file);
	if (check != 12)
	{
		throw string("Network file is not in the correct format");
	}
	weights = new Mat[layers - 1];
	for (int i = 0; i < layers - 1; i++)
	{
		int l1 = sizes[i];
		int l2 = sizes[i + 1];
		weights[i] = Mat(l2, l1);
		for (int j = 0; j < l1; j++)
		{
			for (int k = 0; k < l2; k++)
			{
				weights[i](k, j) = bin::readdouble(file);
			}
		}
	}
	check = bin::readInt(file);
	if (check != 13)
	{
		throw string("Network file is not in the correct format");
	}
}


Network::~Network()
{
	if (this->sizes)
		delete[] this->sizes;
	if (this->weights)
		delete[] this->weights;
	if (this->biases)
		delete[] this->biases;
}

int Network::getDepth()
{
	return layers;
}

int Network::getLayerSize(int layer)
{
	if (layer >= this->layers)
	{
		throw string("Array index error"); // More descriptive
	}
	return sizes[layer];
}

Vec Network::getLayerBiases(int layer)
{
	if (layer >= this->layers - 1)
	{
		throw string("Array index error"); // More descriptive
	}
	return biases[layer];
}

Mat Network::getLayerWeights(int layer)
{
	if (layer >= this->layers - 1)
	{
		throw "Array index error"; // TODO: Be more descriptive
	}
	return weights[layer];
}

Vec Network::feed_forward(Vec & x)
{
	Mat a(x); // Matrix operations return a matrix and not a vector, so we have to work with matrices here
	for (int i = 0; i < layers - 1; i++)
	{
		a = np::sigmoid((weights[i] * a) + biases[i]);
	}
	return Vec(a); // Now we can safely convert back to a vector
}

void Network::train(const vector<Vec*>& x, const vector<Vec*>& y, int epochs, int mini_batch_size, double learning_rate, const vector<Vec*>& tx, const function<bool(int, Vec&)>& pred)
{
	if (x.size() != y.size())
	{
		throw string("x and y sizes must be the same!");
	}
	int n = x.size();
	bool test = tx.size() > 0;

	for (int epoch = 0; epoch < epochs; epoch++)
	{
		// Shuffling x and y
		vector<int> indexes;
		indexes.reserve(n);
		for (int i = 0; i < n; i++) indexes.push_back(i);
		std::random_shuffle(indexes.begin(), indexes.end());
		
		for (int b = 0; b < n; n += mini_batch_size)
		{
			// Creating a mini-batch
			vector<Vec*> _x, _y;
			_x.reserve(mini_batch_size);
			_y.reserve(mini_batch_size);
			for (int i = 0; i < mini_batch_size && b + i < n; i++)
			{
				_x.push_back(x[indexes[b + i]]);
				_y.push_back(y[indexes[b + i]]);
			}

			// "Learning" the mini-batch
			update_mini_batch(_x, _y, learning_rate);

			if (test)
			{
				cout << "Epoch " << epoch << ": " << evaluate(tx, pred) * 100 << "%" << endl;
			}
			else
			{
				cout << "Epoch " << epoch << endl;
			}
		}
	}
}

void Network::save(string file_name)
{
	fstream file;
	file.open(file_name, ios::out | ios::trunc);
	bin::writeInt(file, 10);
	bin::writeInt(file, layers);
	for (int i = 0; i < layers; i++)
	{
		bin::writeInt(file, sizes[i]);
	}
	bin::writeInt(file, 11);
	for (int i = 0; i < layers - 1; i++)
	{
		for (int j = 0; j < sizes[i + 1]; j++)
		{
			bin::writedouble(file, biases[i](j));
		}
	}
	bin::writeInt(file, 12);
	for (int i = 0; i < layers - 1; i++)
	{
		int l1 = sizes[i];
		int l2 = sizes[i + 1];
		for (int j = 0; j < l1; j++)
		{
			for (int k = 0; k < l2; k++)
			{
				bin::writedouble(file, weights[i](k, j));
			}
		}
	}
	bin::writeInt(file, 13);
	file.close();
}

Network & Network::operator=(const Network & ref)
{
	// TODO: insert return statement here
	return *this;
}

void Network::update_mini_batch(vector<Vec*> x, vector<Vec*> y, double learning_rate)
{
	Mat *nb = new Mat[layers - 1];
	Mat *nw = new Mat[layers - 1];

	for (int i = 0; i < layers - 1; i++)
	{
		nb[i] = Mat(biases[i].height(), biases[i].width());
		nw[i] = Mat(weights[i].height(), weights[i].width());
	}

	int n = x.size();

	for (int i = 0; i < n; i++)
	{
		tuple<Mat*, Mat*> deltas = backprop(*x[i], *y[i]);
		Mat *delta_nb = std::get<0>(deltas);
		Mat *delta_nw = std::get<1>(deltas);
		for (int j = 0; j < layers - 1; j++)
		{
			nb[j] = nb[j] + delta_nb[j];
			nw[j] = nw[j] + delta_nw[j];
		}
	}

	for (int i = 0; i < layers - 1; i++)
	{
		biases[i] = biases[i] - ((learning_rate / n) * nb[i]);
		weights[i] = weights[i] - ((learning_rate  / n) * nw[i]);
	}
}

double Network::evaluate(vector<Vec*> x, const function<bool(int, Vec&)>& pred)
{
	if (x.size() == 0)
		return 0;

	int success = 0;
	for (int i = 0; i < x.size(); i++)
	{
		Vec result = feed_forward(*x[i]);
		success += 1 * pred(i, result);
	}
	return (double)success / (double)x.size();
}

tuple<Vec*, Mat*> Network::backprop(Vec & x, Vec & y)
{
	// Constructing zero mats for the weights and biases
	Mat *n_weights = new Mat[layers - 1];
	Vec *n_biases = new Vec[layers - 1];
	for (int i = 0; i < layers - 1; i++)
	{
		n_weights[i] = Mat(getLayerWeights(i).height(), getLayerWeights(i).width());
		n_biases[i] = Vec(getLayerBiases(i).height());
	}

	// Records for the Z values and the activations
	vector<Vec> activations = vector<Vec>();
	vector<Vec> zs = vector<Vec>();
	activations.push_back(x);
	Vec activation = x;

	Vec z, sp;

	// Feedforward through the network
	for (int i = 0; i < layers - 1; i++)
	{
		// Feed forward through a layer and appending the Z and the new activation to the record
		z = (this->weights[i] * activation) + this->biases[i];
		zs.push_back(z);
		activation = np::sigmoid(z);
		activations.push_back(activation);
	}

	int L = layers;

	// Backprop
	Vec delta = cost_derivative(activations[L - 1], y).hadamard(zs[L - 2]);
	n_biases[L - 2] = delta;
	n_weights[L - 2] = delta * activations[L - 2].transpose();

	for (int l = L - 1; l >= 2; l--)
	{
		z = zs[l - 2];
		sp = np::sigmoid_prime(z);
		delta = (this->weights[l - 1].transpose() * delta).hadamard(sp);
		n_biases[l - 2] = delta;
		n_weights[l - 2] = delta * activations[l - 2].transpose();
	}

	return tuple<Vec*, Mat*>(n_biases, n_weights);

	return tuple<Vec*, Mat*>(0, 0);
}

Vec Network::cost_derivative(Vec activations, Vec y)
{
	// Returns the d/dy(C(x)) for the quadratic cost functions
	return activations - y;
}
