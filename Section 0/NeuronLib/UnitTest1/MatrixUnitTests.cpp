#define UNIT_TEST

#include "stdafx.h"
#include "CppUnitTest.h"
#include "Mat.h"

#include <iostream>
#include <string>

using namespace std;
using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace UnitTest1
{		
	TEST_CLASS(MatrixUnitTesting)
	{
	public:
		
		TEST_METHOD(ValidMatrixMatrixAddition)
		{
			double a[][3] = {
				{ 1, 2, 3 },
				{ 6, 4, 2.3},
				{ 1, 9, 9 }
			};
			double b[][3] = {
				{ 5, 2.2, 1.7 },
				{ 0, 8, 3.2 },
				{ -4, 2, 9 }
			};
			Mat ma(3, 3, (double*)a);
			Mat mb(3, 3, (double*)b);
			Mat mr = ma + mb;
			Mat mr2 = mb + ma;
			Assert::IsTrue(mr == mr2);
			double e[][3] = {
				{ 6, 4.2, 4.7 },
				{ 6, 12, 5.5 },
				{ -3, 11, 18 }
			};
			Mat me(3, 3, (double*)e);
			mr.visualize();
			Assert::IsTrue(me == mr);
		}

		TEST_METHOD(InvalidMatrixMatrixAddition)
		{
			Assert::ExpectException<char*>([this] {
				double a[][3] = {
					{ 1, 2, 3 },
					{ 6, 4, 2.3 },
					{ 1, 9, 9 },
					{ 2, 2, 2 },
					{ 0, -4, -3}
				};
				double b[][4] = {
					{ 5, 2.2, 1.7, 3 },
					{ 0, 8, 3.2, 6 },
					{ -4, 2, 9, 8 }
				};
				Mat ma(5, 3, (double*)a);
				Mat mb(3, 4, (double*)b);
				Mat me = ma + mb;
			});
		}
	};
}