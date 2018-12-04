#include <iostream>
#include <fstream>
#include <string>
#include <unordered_set>
#include <unordered_map>
#include <vector>
#include <algorithm>

using namespace std;

struct dataLine {
    bool asleep = false;
    bool awake = false;
    bool startShift = false;
    int ID = 0;
    int month = 0;
    int day = 0;
    int min = 0;

    inline bool operator==(const dataLine& other) const {
        return asleep == other.asleep && awake == other.awake && startShift == other.startShift && ID == other.ID && day == other.day && min == other.min;
    }
};

void partOne();
void partTwo();
dataLine populateStruct(string x);
bool dataLineCompare(dataLine lhs, dataLine rhs);

int main() {
    unordered_map<string, vector<dataLine>> map; // map from a date to a vector of structs 
    unordered_map<int, vector<int>> count; // tracks the sleeping time for specific IDs
    ifstream myfile ("input.txt");
	string input = "";
	if (myfile.is_open()) {
        while (true) {
            int end = 3;
            string together = "";
            for(int i = 0; i < end; i++) {
                myfile >> input;
                if(myfile.eof()) { break; }
                together += " " + input;
                if(i == 2) {
                    if(input.substr(0,1) == "G")
                        end = 6;
                    else if(input.substr(0,1) == "f" || input.substr(0,1) == "w")
                        end = 4;
                }
            }
            if(myfile.eof()) { break; }
            dataLine dataStruct = populateStruct(together.substr(1,together.size() - 1));
            if(map.find(to_string(dataStruct.month) + "/" + to_string(dataStruct.day)) == map.end()) {
                vector<dataLine> vec; 
                vec.push_back(dataStruct);
                map.insert({(to_string(dataStruct.month) + "/" + to_string(dataStruct.day)), vec});
            } else {
                map[(to_string(dataStruct.month) + "/" + to_string(dataStruct.day))].push_back(dataStruct);
            }
        }
        unordered_map<string, vector<dataLine>>:: iterator p;
        for(p = map.begin(); p != map.end(); p++) {
            std::sort(p->second.begin(), p->second.end(), dataLineCompare);
            vector<dataLine> vec = p->second;
            int ID = vec.at(0).ID;
            for(int i = 1; i < vec.size(); i += 2) {
                if(count.find(ID) == count.end()) {
                    vector<int> x;
                    x.push_back(vec.at(i+1).min - vec.at(i).min);
                    x.push_back(vec.at(i).min);
                    x.push_back(vec.at(i+1).min);
                    count.insert({ID, x});
                } else {
                    count[ID].at(0) += vec.at(i+1).min - vec.at(i).min;
                    count[ID].push_back(vec.at(i).min);
                    count[ID].push_back(vec.at(i + 1).min);
                }
            }
        }
        int bestID = 0;
        int bestCount = 0;
        unordered_map<int, vector<int>>:: iterator q;
        for(q = count.begin(); q != count.end(); q++) {
            if(q->second.at(0) > bestCount) {
                bestCount = q->second.at(0);
                bestID = q->first;
            }
        }
        int arr[60];
        for(int i = 0; i < 60; i++) {
            arr[i] = 0;
        }
        for(int i = 1; i < count[bestID].size(); i += 2) {
            for(int j = count[bestID][i]; j < count[bestID][i+1]; j++) {
                arr[j]++;
            }
        }
        int index = 0; int max = 0;
        for(int i = 0; i < 60; i++) {
            if(arr[i] > max) {
                max = arr[i];
                index = i;
            }
        }
        cout << "Guard who sleeps the most ID: " << bestID << "." << endl << "Minute with the highest frequency of the guard sleeping: " << index << endl;
        cout << "Checksum: " << bestID * index << endl;
        
        // part two

        int highestFrequency = 0; int whatMinute = 0;
        for(q = count.begin(); q != count.end(); q++) {
            int arr[60];
            for(int i = 0; i < 60; i++) {
                arr[i] = 0;
            }
            for(int i = 1; i < count[q->first].size(); i += 2) {
                for(int j = count[q->first][i]; j < count[q->first][i+1]; j++) {
                    arr[j]++;
                }
            }
            int index = 0; int max = 0;
            for(int i = 0; i < 60; i++) {
                if(arr[i] > max) {
                    max = arr[i];
                    index = i;
                }
            }
            if(highestFrequency < max) {
                highestFrequency = max;
                whatMinute = index;
                bestID = q->first;
            }
        }
        cout << endl << "Guard ID who consistently sleeps on the same single minute the most: " << bestID << " during minute " << whatMinute;
        cout << "." << endl << "Chance that they will be asleep on that minute when they sleep: " << (double) highestFrequency / (count[bestID].size() - 1) << "." << endl;
        cout << "Checksum: " << bestID * whatMinute << endl;
    }
}

bool dataLineCompare(dataLine lhs, dataLine rhs) {
    return lhs.min < rhs.min;
}

dataLine populateStruct(string x) {
    int monthLength[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    dataLine t;
    t.month = atoi(x.substr(6,2).c_str());
    t.min = atoi(x.substr(15,2).c_str());
    if(atoi(x.substr(13,1).c_str()) == 0) 
        t.day = atoi(x.substr(9,2).c_str());
    else {
        t.day = atoi(x.substr(9,2).c_str()) + 1;
        t.min = -1;
        if(monthLength[t.month - 1] < t.day) {
            t.month++;
            t.day = 1;
            if(t.month == 13) 
                t.month = 1;
        }
    }
    if(x.substr(19,1) == "w") {
        t.awake = true;
    } else if (x.substr(19,1) == "f") {
        t.asleep = true;
    } else if (x.substr(19,1) == "G") {
        t.startShift = true;
        t.ID = atoi(x.substr(26,x.find(" ", 26) - 26).c_str()); 
    }
    //cout << t.month << " " << t.day << " " << t.min << endl;
    return t;
}