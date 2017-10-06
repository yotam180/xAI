#include "Network.h"
#include <fstream>

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
		cout << "A after layer " << (i + 1) << endl;
		a = np::sigmoid((weights[i] * a) + biases[i]);
		a.visualize();
	}
	return Vec(a); // Now we can safely convert back to a vector
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
