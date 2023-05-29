#include <iostream>
#include <vector>
using namespace std;

void rotate(vector<vector<int>>& matrix) {
    int n = matrix.size();
   
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            
            swap(matrix[i][j], matrix[j][i]);
        }
    }
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n / 2; j++) {
            swap(matrix[i][j], matrix[i][n - 1 - j]);
        }
    }
}

int main() {
    int n;
    cout << "Enter the size of matrix: ";
    cin >> n;
    vector<vector<int> > matrix(n, vector<int>(n));
    cout << "Enter the elements of matrix: " << endl;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> matrix[i][j];
        }
    }
    cout << "Before rotation:" << endl;
    for (auto row : matrix) {
        for (auto elem : row) {
            cout << elem << "\t";
        }
        cout << endl;
    }
    rotate(matrix);
    cout << "After rotation:" << endl;
    for (auto row : matrix) {
        for (auto elem : row) {
            cout << elem << "\t";
        }
        cout << endl;
    }
}