#include <iostream>
#include <fstream>
#include <string>
#include <unordered_set>
#include <unordered_map>

void partOne();
void partTwo();

using namespace std;

int main() {
	partOne();	
	partTwo();
}
	
void partOne() {
	int width = 1000;
	int height = 1000;
	ifstream myfile ("input.txt");
	int *grid = new int[width * height];
	string input = "";
	if (myfile.is_open()) {
		while (true) {
			int x = 0; int y = 0;
			int wid = 0; int ht = 0;
			for(int i = 0; i < 4; i++) {
				myfile >> input;
				if (i == 2) {
					x = atoi(input.substr(0, input.find(",")).c_str());
					y = atoi(input.substr(input.find(",") + 1, input.size() - input.find(",")).c_str());
				}
				if (i == 3) {
					wid = atoi(input.substr(0, input.find("x")).c_str());
					ht = atoi(input.substr(input.find("x") + 1, input.size() - input.find("x")).c_str());
				}
			}
			if(myfile.eof()) 
				break;
			for(int i = 0; i < wid; i++) {
				for(int j = 0; j < ht; j++) {
					*(grid + ((j + y) * width) + x + i) += 1;
				}
			}
		}
		int count = 0;
		for(int i = 0; i < width; i++) {
			for(int j = 0; j < height; j++) {
				if(*(grid + (i * width) + j) > 1) 
					count++;
				}
		}
		cout << "Sq Foot Overlapped: " << count << endl;
	}
	myfile.close();
	delete grid;
}

// Keep all IDs in a set. Go through potential data, and add singular indexes to the hashmap with the index as the key and data's ID for the value.
// If a value already exists in the map, we have a conflict and we remove both IDs from the set. Prune set until we get only IDs with a unique area.
void partTwo() {
	unordered_set<string> set;
	unordered_map<int, string> map;
	int width = 1000;
	int height = 1000;
	ifstream myfile ("input.txt");
	string input = "";
	if (myfile.is_open()) { 
		while (true) {
			int x = 0; int y = 0;
			int wid = 0; int ht = 0;
			string ID = "";
			for(int i = 0; i < 4; i++) {
				myfile >> input;
				if (i == 0) {
					ID = input.substr(1,input.size() - 1);
					set.insert(ID);
				}
 				if (i == 2) {
					x = atoi(input.substr(0, input.find(",")).c_str());
					y = atoi(input.substr(input.find(",") + 1, input.size() - input.find(",")).c_str());
				}
				if (i == 3) {
					wid = atoi(input.substr(0, input.find("x")).c_str());
					ht = atoi(input.substr(input.find("x") + 1, input.size() - input.find("x")).c_str());
				}
			}
			if(myfile.eof()) 
				break;
			for(int i = 0; i < wid; i++) {
				for(int j = 0; j < ht; j++) {
					if(map.find((j + y) * width + x + i) != map.end()) { 
						if(set.find(ID) != set.end())
							set.erase(set.find(ID));
						string temp = map.find((j + y) * width + x + i)->second;
						if(set.find(temp) != set.end())
							set.erase(set.find(temp));
					}
					else {
						map.insert({(j + y) * width + x + i, ID});
					}
				}
			}
		}
		cout << "ID with unique area: " << *(++set.begin()) << endl;
	}
	myfile.close();
}
