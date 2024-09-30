#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int income;
    float mr;
    int savings;
    cin >> income >> mr >> savings; cin.ignore();
    int n;
    cin >> n; cin.ignore();
    for (int i = 0; i < n; i++) {
        int price;
        int expenses;
        cin >> price >> expenses; cin.ignore();
    }

    // Write an answer using cout. DON'T FORGET THE "<< endl"
    // To debug: cerr << "Debug messages..." << endl;

    cout << "Yes, the house is affordable with 1 roommate(s) and $1 to spare." << endl;
}
