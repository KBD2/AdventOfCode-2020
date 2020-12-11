#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <map>

std::map<int, uint64_t> cache;

uint64_t branch(int current, std::vector<int> &adaptors)
{
    std::vector<int> possible;
    uint64_t subtotal = 0;

    for (auto item = adaptors.begin(); item != adaptors.end(); item++)
    {
        if (current < *item && *item < current + 4)
        {
            possible.push_back((int)std::distance(adaptors.begin(), item));
        }
    }
    if (possible.size() == 0) subtotal++;
    for (auto item = possible.begin(); item != possible.end(); item++)
    {
        if (cache.find(adaptors[*item]) != cache.end())
        {
            subtotal += cache[adaptors[*item]];
        }
        else subtotal += branch(adaptors[*item], adaptors);
    }

    cache[current] = subtotal;

    return subtotal;
}

int main()
{
    std::ifstream input("input.txt");
    std::vector<int> adaptors;
    uint64_t total;

    for(std::string line; std::getline(input, line);)
    {
        adaptors.push_back(std::stoi(line));
    }
    total = branch(0, adaptors);
    std::cout << total << std::endl;
    std::cin.get();
}