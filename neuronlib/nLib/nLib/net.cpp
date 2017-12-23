#include "net.h"

net * new_net(int layers, int * sizes)
{
	// Allocating a new network
	net *n = (net*)malloc(sizeof(net));
	
	// Failsafe allocation
	if (!n) {
		return NULL;
	}

	n->layers = layers;
	n->sizes = (int*)malloc(sizeof(int) * layers);
}
