#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int w;
    cin >> w; cin.ignore();
    for (int i = 0; i < w; i++) {
        string wall;
        getline(cin, wall);
    }
    int d;
    cin >> d; cin.ignore();
    for (int i = 0; i < d; i++) {
        string door;
        getline(cin, door);
    }

    // Write an answer using cout. DON'T FORGET THE "<< endl"
    // To debug: cerr << "Debug messages..." << endl;

    cout << "0 C4 needed to go through 0 walls" << endl;
}
