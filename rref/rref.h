// Reduced Row Echelon Form Calculator in C++
// Javin Zipkin
#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

// Function prototypes
vector<double> split(string line, char delim);
bool makePivot(vector<vector<double>>& mat, int top, int col);
void swap(vector<vector<double>>& vec, int rowA, int rowB);
void addRow(vector<vector<double>>& vec, int rowA, int rowB, double factor);
void scaleRow(vector<vector<double>>& vec, int row, double factor);
void applyPivot(vector<vector<double>>& mat, int pivRow, int pivCol);
void printVector(vector<vector<double>>& vec);
bool compareFloat(float x, float y);
void rref(vector<vector<double>>& mat, int verbose = 0);