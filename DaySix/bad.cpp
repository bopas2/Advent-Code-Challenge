#include <iostream>
#include <fstream>
#include <vector>
#include <tuple>
#include <climits>

using namespace std;

struct coordinate {
    unsigned short x;
    unsigned short y;
    coordinate() { }
    coordinate(unsigned short x, unsigned short y) {
        this->x = x;
        this->y = y;
    }
};

/*
 * Parses the input file according to the given filename and adds all parsed
 * nodes into the coordinate vector given
 */
void parseInput(string filename, std::vector<coordinate> &coords) {
    string currentLine; // current line
    ifstream instream; // input stream
    instream.open(filename);
    if (instream.is_open()) {
        while (std::getline(instream, currentLine)) {
            int comma = currentLine.find_first_of(",");
            unsigned short x = std::atoi(currentLine.substr(0, comma).c_str());
            unsigned short y = std::atoi(currentLine.substr(comma + 2).c_str());
            coords.push_back(coordinate(x, y));
        }
    }
    instream.close();
}

/**
 * Finds the outer bounds of the given vector of coordinates, returning a tuple
 * of <width, height>
 */
std::tuple<coordinate, coordinate> findBounds(std::vector<coordinate> &coords) {
    coordinate min = coordinate(USHRT_MAX, USHRT_MAX);
    coordinate max = coordinate(0, 0);
    for (const auto &coord : coords) {
        if (coord.x > max.x) max.x = coord.x;
        if (coord.y > max.y) max.y = coord.y;
        if (coord.x < min.x) min.x = coord.x;
        if (coord.y < min.y) min.y = coord.x;
    }
    return std::make_tuple(min, max);
}

inline unsigned short manhattanDistance(coordinate &a, coordinate &b) {
    // abs(Dy) + abs(Dx)
    return (unsigned short) (std::abs(a.x - b.x) + std::abs(a.y - b.y));
}

/**
 * Finds the closest node to the given coordinates, using manhattan distance as
 * the distance function
 */
short findClosestNode(coordinate &coord, std::vector<coordinate> &nodes) {
    short closestIndex = -1;
    unsigned short closestDistance = USHRT_MAX; // begin at the max (32k)
    bool isUnique = true;
    for (short i = 0; i < nodes.size(); ++i) {
        unsigned short distance = manhattanDistance(coord, nodes[i]);
        if (distance < closestDistance) {
            closestIndex = i;
            closestDistance = distance;
            isUnique = true;
        } else if (distance == closestDistance) {
            isUnique == false;
        }
    }
    // if the closest node isn't unique, return -1
    return isUnique ? closestIndex : -1;
}

short* findAreas(coordinate &min, coordinate &max, std::vector<coordinate> &nodes) {
    const int width = max.x - min.x + 1;
    const int height = max.y - min.y + 1;

    // array of areas of voroni fragments where the index is the node index
    short* fragmentAreas = new short[nodes.size()];
    std:fill(fragmentAreas, fragmentAreas + sizeof(fragmentAreas), 0);
    for (int i = 0; i < width; ++i) {
        // whether the current i iteration is on the border
        bool isXBorder = (i == 0) || (i == width - 1);
        for (int j = 0; j < height; ++j) {
            // whether the current i,j iteration is on the border
            bool isBorder = isXBorder || (j == 0) || (j == height - 1);
            coordinate c = coordinate(i + min.x, j + min.y);
            short closestNode = findClosestNode(c, nodes);
            // if the position 'belongs' to a node,
            if (closestNode >= 0) {
                // if it falls on the border (would extend into infinum),
                // 'poison' the area of the fragment to mark it as invalid by
                // setting it to the short minimum (-32k)
                if (isBorder) fragmentAreas[closestNode] = SHRT_MIN;
                // else, increment the fragment area
                else ++fragmentAreas[closestNode];
            }
        }
    }
    return fragmentAreas;
}

int main() {
    std::vector<coordinate> nodes;
    parseInput("input.txt", nodes);
    std::tuple<coordinate, coordinate> bounds = findBounds(nodes);
    coordinate min = std::get<0>(bounds);
    coordinate max = std::get<1>(bounds);

    //addPadding(min, max, 1);
    cout << nodes.size() << " nodes parsed; bounds: x "
            << min.x << "-" << max.x << "; y "
            << min.y << "-" << max.y << endl;
    short* areas = findAreas(min, max, nodes);
    short maxArea = 0;
    for (size_t i = 0; i < nodes.size(); ++i) {
        if (areas[i] > 0) { // if the node's fragment wasn't infinite
            cout << "i: " << i << "; area: " << areas[i] << endl;
        }
        if (areas[i] > maxArea) maxArea = areas[i];
    }
    delete [] areas;

    cout << "maxArea: " << maxArea << endl;
    return 0;
}
