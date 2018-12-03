#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
	int *grid = new int[1000 * 1000];
	*(grid + 2) = 3;
	cout << grid[2] << endl;
	return 0;
}
