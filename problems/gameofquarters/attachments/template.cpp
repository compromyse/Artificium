#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int number_of_rounds;
    cin >> number_of_rounds; cin.ignore();
    for (int i = 0; i < number_of_rounds; i++) {
        string alice_sequence;
        string bob_sequence;
        string round_tosses;
        cin >> alice_sequence >> bob_sequence >> round_tosses; cin.ignore();
    }

    // Write an answer using cout. DON'T FORGET THE "<< endl"
    // To debug: cerr << "Debug messages..." << endl;

    cout << "WINNER!" << endl;
}
