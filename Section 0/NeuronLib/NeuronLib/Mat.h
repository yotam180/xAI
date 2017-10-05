#pragma once
class Mat
{
public:
	Mat();
	Mat(int width, int height);
	Mat(const Mat& ref);
	~Mat();

	int height();
	int width();

	void visualize();

	float& operator()(int x, int y) const;
	Mat& operator=(const Mat& ref);


private:
	int h, w;
	float* vals;
};

