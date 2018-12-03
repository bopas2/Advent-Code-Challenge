#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main () {
  char output[26];
  ifstream myfile ("input.txt");
  int num2 = 0;
  int num3 = 0;
  int countLog[26];
  if (myfile.is_open()) {
    while (!myfile.eof()) {
    	for(int i = 0; i < 26; i++) {
    		countLog[i] = 0;
		}
    	myfile >> output;
    	for(int i = 0; i < 26; i++) {
    		countLog[output[i] - 'a'] += 1;
		}
		bool notTwo = false;
		bool notThree = false;
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
  cout << "Frequency count of 2: " << num2 << "." << endl << "Frequency count of 3: " << num3 << endl;
  cout << "Checksum: " << num2 * num3;
  return 0;
}

