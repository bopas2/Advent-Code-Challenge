#include <iostream>
#include <fstream>
#include <string>
#include <unordered_set>
#include <unordered_map>
#include <vector>
#include <algorithm>

using namespace std;

int width = 360;
int ht = 360;

struct Node {
    int area = 0;
    int x;
    int y;
    bool notEdge = true;
    Node(int xIn, int yIn) {
        x = xIn;
        y = yIn;
    }
    bool operator==(const Node& nod) {
        return x == nod.x && y == nod.y && area == nod.area;
    }
};

void findClosest(vector<Node> &vect, int x, int y);
            
int main() {
    vector<Node> coords;
    ifstream myfile ("input.txt");
	string x1 = ""; string y1 = ""; 
	if (myfile.is_open()) {
        while (true) {
            myfile >> x1; 
            myfile >> y1;
            if(myfile.eof()) { break; }
            Node x {stoi(x1.substr(0,x1.find(","))), stoi(y1)};
            coords.push_back(x);
        }

        for(int i = 0; i < width; i++) {
            for(int j = 0; j < ht; j++) {
                findClosest(coords, i, j);
            }
        }
        int min = 0;
        for(int i = 0; i < coords.size(); i++) {
            if(coords[i].area > min && coords[i].notEdge) {
                min = coords[i].area;
            }
        }
        cout << "Area of Node with Greatest Area: " << min << endl;
        int totalCloseArea = 0;
        for(int i = 0; i < width; i++) {
            for(int j = 0; j < ht; j++) {
                int dist = 0;
                for(int c = 0; c < coords.size(); c++) {
                    dist += abs(i - coords[c].x) + abs(j - coords[c].y);
                }
                if(dist < 10000) { 
                    totalCloseArea++; 
                }
            }
        }
        cout << "Places less than 10000 units from a node: " << totalCloseArea << endl;
        myfile.close();
    }
    return 0;
}

void findClosest(vector<Node> &vect, int x, int y) {
    vector<Node> closest;
    int smallestDist = numeric_limits<int>::max();
    for(int i = 0; i < vect.size(); i++) {
        int dist = abs(vect[i].x - x) + abs(vect[i].y - y);
        if(abs(dist < smallestDist)) {
            smallestDist = dist;
            closest.clear();
            closest.push_back(vect[i]);
        } else if(dist == smallestDist) {
            closest.push_back(vect[i]);
        }
    }
    for(int i = 0; i < closest.size(); i++) {
        for(int j = 0; j < vect.size(); j++) {
            if(closest.size() <= 1) {
                if(vect[j] == closest[i]) {
                    vect[j].area++;
                    if(x == 0 || x == width - 1 || y == 0 || y == ht - 1) {
                        vect[j].notEdge = false;
                    }
                }
            }
        }
    }
}