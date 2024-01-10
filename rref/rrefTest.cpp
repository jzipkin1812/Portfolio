// Testing the RREF function in C++
// Javin Zipkin
#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include "rref.h"
#include <fstream>
using namespace std;
int main(int argc, char* argv[])
{
    // Simple Cases
    vector<vector<double>> easy1 = {{2, 10, 2}, 
                                    {2, 11, 5}};
    vector<vector<double>> easy2 = {{2, 10, 2}, 
                                    {2, 13, 5}};
    vector<vector<double>> easy3 = {{4, 20, 4}, 
                                    {2, 13, 5},
                                    {4, 3, 12}};
    vector<vector<double>> easy4 = {{0, 17, -8}, 
                                    {2, 13, 5},
                                    {4, 3, 12}};
    
    // Cases with Free Variables
    vector<vector<double>> free1 = {{3, 3}, 
                                    {2, 2}};
    vector<vector<double>> free2 = {{-2, 8}, 
                                    {3,  2},
                                    {4, -1},
                                    {5,  2}};
    // Harder Cases with rows or columns of 0s or free variable columns
    // that are in between pivot columns
    // Column of 0s
    vector<vector<double>> hard1 = {{5, 0, 0}, 
                                    {0, 0, 4},
                                    {3, 0, 4}}; 
    // Free Variable column in between pivot columns                              
    vector<vector<double>> hard2 = {{2, 2, 2, 2}, 
                                    {1, 2, 4, 1},
                                    {5, 7, 11, 8}};    
    // Row of 0s
    vector<vector<double>> hard3 = {{2, 2, 3, 1}, 
                                    {2, 2, 3, 1},
                                    {4, 3, 2, 8}};
    // Stuff on the left
    vector<vector<double>> totheLeft = {{-6, 1, 0, 0}, 
                                              {-4, 0, 1, 0},
                                              { 5, 0, 0, 1}};  

    // Some Edge Cases
    vector<vector<double>> empty = {{}, {}};
    vector<vector<double>> oneRow = {{5, 2, 3, 4, 5}};
    vector<vector<double>> oneCol = {{0}, {2}, {3}, {3}};
    vector<vector<double>> reducedAlready = {{1, 0, 0, 2}, {0, 1, 0, 3}, {0, 0, 1, 0}, {0, 0, 0, 0}};

    // Opening a Matrix from a Text File
    vector<vector<double>> fromFile;
    ifstream ifs;
    string line;
    ifs.open("rref.txt");
    while(getline(ifs, line))
    {
        fromFile.push_back(split(line, ' '));
    }
    ifs.close();

    if(argc > 1)
    {
        rref(fromFile, stoi(argv[1]));
    }
    else
    {
        rref(fromFile, 0);
    }
    
    printVector(fromFile);
    return(0);
}