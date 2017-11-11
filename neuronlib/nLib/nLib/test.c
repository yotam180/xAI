#include <stdio.h>
#include <stdlib.h>

#include "mat.h"

int main(void)
{
	mat *a = zero_mat(4, 2);
	visualize_int_mat(a);
	system("pause");
	free(a);
	return 0;
}