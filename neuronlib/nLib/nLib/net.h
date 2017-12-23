#ifndef NET
#define NET
#endif

#include "mat.h"

#include <stdio.h>
#include <stdlib.h>

typedef struct net {
	int layers;
	int *sizes;

	vec_p *biases;
	mat_p *weights;
} net;

net *new_net(int layers, int* sizes);
void free_net(net *ref);
vec_p feed_forward(net *net, vec_p *x);

