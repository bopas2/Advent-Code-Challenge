#include <iostream>
#include <fstream>
#include <string>
#include <unordered_set>
using namespace std;

void partOne();
void partTwo();

int main() {
	partOne();
	partTwo();
	return 0;
}

void partOne () {
  char input[26];
  ifstream myfile ("input.txt");
  int num2, num3 = 0;
  int countLog[26];
  if (myfile.is_open()) {
    while (true) {
    	bool notTwo = false;
		bool notThree = false;
		for(int i = 0; i < 26; i++) 
    		countLog[i] = 0;
    	myfile >> input;
    	if(myfile.eof()) 
			break;
    	for(int i = 0; i < 26; i++) 
    		countLog[input[i] - 'a'] += 1;
		for(int i = 0; i < 26; i++) {
    		if(countLog[i] == 2 && !notTwo) {
    			num2 += 1;
    			notTwo = true;
			} 
			else if(countLog[i] == 3 && !notThree) {
				num3 += 1;
				notThree = true;
			}
		}
    }
    myfile.close();
  }
  cout << "---" << endl;
  cout << "Part One" << endl;
  cout << "Frequency count of 2: " << num2 << "." << endl << "Frequency count of 3: " << num3 << endl;
  cout << "Checksum: " << num2 * num3 << endl;
  cout << "---" << endl;
}

void partTwo() {
	ifstream myfile ("input.txt");
	char input[26];
	unordered_set<string> sets[26];
	if (myfile.is_open()) {
		while (true) {
			myfile >> input;
			if(myfile.eof()) 
				break;
			for(int i = 0; i < 26; i++) {
				string s = "";
				for(int j = 0; j < 26; j++) {
					if(j != i) 
						s += input[j]; 
				}
				if (sets[i].count(s) == 1) {
					cout << "Part Two" << endl;
					cout << "Common letters in the ID: " << s;
					return;
				}
				sets[i].insert(s);
			}
		}
	}
}

