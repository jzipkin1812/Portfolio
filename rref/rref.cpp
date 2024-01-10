// Reduced Row Echelon Form Calculator in C++
// Javin Zipkin
#include <iostream>
#include <vector>
#include <iomanip>
#include <cmath>
#include <string>
#include <fstream>
using namespace std;

// Function prototypes
bool makePivot(vector<vector<double>>& mat, int top, int col);
void swap(vector<vector<double>>& vec, int rowA, int rowB);
void addRow(vector<vector<double>>& vec, int rowA, int rowB, double factor);
void scaleRow(vector<vector<double>>& vec, int row, double factor);
void applyPivot(vector<vector<double>>& mat, int pivRow, int pivCol);
void printVector(vector<vector<double>>& vec);
bool compareFloat(float x, float y);
void rref(vector<vector<double>>& mat);
vector<double> split(string line, char delim);

// FILE PROCESSING
vector<double> split(string line, char delim)
{
    vector<double> result; // final result
    string temp; // temporary "line" holder that will hold each word
    stringstream stream(line); // the entire line of text from the file
    while(getline(stream, temp, delim))
    {
        result.push_back(stod(temp));
    }
    return(result);
}

// ELEMENTARY ROW OPERATIONS
void swap(vector<vector<double>>& vec, int rowA, int rowB)
{
    vector<double> temp = vec[rowA];
    vec[rowA] = vec[rowB];
    vec[rowB] = temp;
}
void addRow(vector<vector<double>>& vec, int rowA, int rowB, double factor)
{
    for(int col = 0; col < vec[0].size(); col++)
    {
        vec[rowB][col] += vec[rowA][col] * factor;
    }
}
void scaleRow(vector<vector<double>>& vec, int row, double factor)
{
    for(double& entry : vec[row])
    {
        entry *= factor;
    }
}

// Precondition: 2D Vector with at least 1 row and 1 column
// Postcondition: Matrix is converted into Reduced Row Echelon Form
void rref(vector<vector<double>>& mat, int verbose = 0)
{
    int pivotRow = 0;
    int pivotCol = 0;
    bool madePivot;
    const int height = mat.size();
    const int width = mat[0].size();
    // Check for unsatisfied precondition
    if(width < 1 || height < 1)
    {
        cerr << "Cannot reduce empty matrix" << endl;
        return;
    }
    if(verbose)
    {
        printVector(mat);
    }
    // While the algorithm has not reached the end of the matrix...
    while(pivotRow < height && pivotCol < width)
    {
        // make a pivot in the current column
        // OR, figure out that the current column is a free variable column
        madePivot = makePivot(mat, pivotRow, pivotCol);
        // If it's a pivot column, make the other entries in the column 0
        if(madePivot)
        {
            if(verbose)
            {
                cout << "MAKING PIVOT..." << endl;
                printVector(mat);
                cout << "APPLYING PIVOT..." << endl;
                applyPivot(mat, pivotRow, pivotCol);
                printVector(mat);
            }
            else
            {
                applyPivot(mat, pivotRow, pivotCol);
            }
        }
        // If it's a free variable column, move on to the next column
        else
        {
            pivotCol++;
            continue;
        }
        // If it was a pivot column, move on to the next column
        // AND move on to the next row (down and to the right)
        pivotRow++;
        pivotCol++;
    }

}

// Precondition: 2D Matrix, the desired row for the pivot to move to, and the column to find a pivot in
// Postcondition: A pivot will be created, moved to the requested row, and scaled down to 1
// Postcondition: Returns "False" if the column is a FREE VARIABLE column
bool makePivot(vector<vector<double>>& mat, int top, int col)
{
    // Top = the row that this pivot will rest on
    // Col = the pivot column
    int pivotRow = top; // Start at the top and move down to
    // Find a nonzero entry in the selected column
    while(compareFloat(mat[pivotRow][col], 0.0))
    {
        // If row is all 0s, try moving to the next row
        pivotRow++;
        // If the column down is all 0s, it's a free variable column, return FALSE
        if(pivotRow >= mat.size())
        {
            return(false);
        }
    }
    // Now we know the pivot row and column. 
    // Scale it to 1 
    scaleRow(mat, pivotRow, 1.0 / mat[pivotRow][col]);
    // and move it to the top
    swap(mat, pivotRow, top);
    return(true);
}

// Precondition: The location of the pivot in the matrix, and the pivot entry is 1
// Postcondition: All numbers above and below the pivot will become 0
void applyPivot(vector<vector<double>>& mat, int pivRow, int pivCol)
{
    double factor;
    int rowNum = 0;
    for(vector<double>& rowToApply : mat)
    {
        // If the entry is nonzero, apply the pivot to it and make it zero
        if(rowToApply[pivCol] != 0 && rowNum != pivRow)
        {
            factor = -1 * (rowToApply[pivCol]);
            addRow(mat, pivRow, rowNum, factor);
            
        }
        rowNum++;
    }
}


// Utility Functions
void printVector(vector<vector<double>>& vec)
{
    for(vector<double> row : vec)
    {
        for(double& entry : row)
        {
            // Weird processing for weird negative 0 situations
            if(compareFloat(entry, 0))
            {
                entry = 0;
            }
            
            cout << entry << "\t";
        }
        cout << endl;
    }
    cout << "------------------------------" << endl;
}
bool compareFloat(float x, float y)
{
    return(fabs(x - y) < 0.001);
}
