#include <iostream>
#include <fstream>
#include <string>
#include <unordered_set>
#include <unordered_map>
#include <vector>
#include <algorithm>

using namespace std;

string getParsedData(string input);

int main() {
    ifstream myfile ("input.txt");
	string input = "";
	if (myfile.is_open()) {
        myfile >> input;
        myfile.close();
    }
    cout << "Number of polymer units remaining after reaction: " << getParsedData(input).size() << endl;
    int min = numeric_limits<int>::max();
    for(int i = 65; i < 65 + 26; i++) {
        string temp = input;
        char a = i; 
        char b = 32 + i;
        int count = 0;
        for(string::iterator it = temp.begin(); it <= temp.end(); ++it) {
            while(true) {
                if((*it) == a || (*it) == b) {
                    it = temp.erase(it);
                    if(it > temp.end()) { break; }
                } else { break; }
            }
            count++;
        }
        int t = getParsedData(temp).size();
        if(t < min) { min = t;} 
    }
    cout << "Smallest possible number of polymer units with a certain polymer type removed: " << min << endl;
}

string getParsedData(string input) {
    for(string::iterator it = input.end(); it >= input.begin(); --it) {
        while(true) {
            int diff = toupper((*it)) - tolower((*it));
            if((it - 1) != input.begin() - 1) {
                if((*it) - diff == *(it - 1) || (*it) + diff == *(it - 1)) {
					it = input.erase(it);
					it = input.erase(it - 1);
                } else { 
                    break; 
                }
            } else { break; }
        }
    }
    return input; 
}
